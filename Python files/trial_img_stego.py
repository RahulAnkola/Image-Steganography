from PIL import Image
import cv2


def int2bin(rgb):
    r, g, b = rgb
    return ('{0:08b}'.format(r),
            '{0:08b}'.format(g),
            '{0:08b}'.format(b))


def bin2int(rgb):
    r, g, b = rgb
    return (int(r, 2),
            int(g, 2),
            int(b, 2))


def merge2rgb2(rgb1, rgb2):

    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    rgb = (r1[:6] + r2[:2],
           g1[:6] + g2[:2],
           b1[:6] + b2[:2])
    return rgb


def merge2img2(img1, img2):

    image1 = img1
    image2 = img2

    # Condition for merging
    if(image1.size[0] > image2.size[0] or image1.size[1] > image2.size[1]):
        print("Cannot merge as the size of 1st Image is greater than size of 2nd Image")
        return

   # Getting the pixel map of the two images
    pixel_tuple1 = image1.load()
    pixel_tuple2 = image2.load()
    # print(pixel_tuple1)
    # print(pixel_tuple2)

    # The new image that will be created.
    # Setting the size of Image 2 as Image 1 will be merged to Image 2.
    new_image = Image.new(image2.mode, image2.size)
    # print(image2.mode)
    pixels_new = new_image.load()

    for row in range(image2.size[0]):
        for col in range(image2.size[1]):

            rgb1 = int2bin(pixel_tuple2[row, col])
            # print(pixel_tuple2[row,col])

            # Using a black pixel as default
            rgb2 = int2bin((0, 0, 0))

            # Converting the pixels of image 1 if condition is satisfied

            if(row < image1.size[0] and col < image1.size[1]):
                rgb2 = int2bin(pixel_tuple1[row, col])

            merge_rgb = merge2rgb2(rgb1, rgb2)

            pixels_new[row, col] = bin2int(merge_rgb)

    # print('rahul')
    new_image.convert('RGB').save('merged2.jpg')
    # print(new_image.size[0],"  ",new_image.size[1])
    return new_image


def unmerge2(img):

    pixel_map = img.load()

    new_image = Image.new(img.mode, img.size)
    pixels_new = new_image.load()

    original_size = img.size
    print("hello: ", original_size)
    for row in range(img.size[0]):
        for col in range(img.size[1]):
            r, g, b = int2bin(pixel_map[row, col])

            # Extracting the last 6 bits (corresponding to the hidden image) and adding zeroes to increase the brightness.

            rgb = (r[6:] + "000000",
                   g[6:] + "000000",
                   b[6:] + "000000")

            # Convert it to an integer tuple
            pixels_new[row, col] = bin2int(rgb)

           # If this is a 'valid' position, store it as a last valid option
            if pixels_new[row, col] != (0, 0, 0):
                original_size = (row + 1, col + 1)

    # Crop the image based on the 'valid' pixels
    new_image = new_image.crop((0, 0, original_size[0], original_size[1]))
    new_image.convert('RGB').save('unmerged2.jpg')
    return new_image


def main():
    image1 = Image.open('waterfall2.jpg')
    image2 = Image.open('sunset2.jpg')

    merged_image2 = merge2img2(image1, image2)
    unmerged_image2 = unmerge2(merged_image2)


main()
