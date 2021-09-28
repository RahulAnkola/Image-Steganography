import cv2
import numpy as n


def intToBinary(msg):
    binary = [format(i, "08b") for i in msg]
    return binary  # list


def binaryToInt(rgb):
    r, g, b = rgb
    rgb = (int(r, 2), int(g, 2), int(b, 2))
    rgb = n.asarray(rgb)
    return rgb


def mergeRGB(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    rgb = (r2[:6] + r1[:2],
           g2[:6] + g1[:2],
           b2[:6] + b1[:2])
    return rgb  # tuple


def merge(img1, img2):
    if img1.shape[0] > img2.shape[0] or img1.shape[1] > img2.shape[1]:
        print("Reduce the size of embedding image or increase the size of cover image")
        return
    row = -1
    col = -1
    for i in img2:  # gives rows
        row += 1
        col = -1
        for pixel in i:  # gives column
            col += 1
            rgb2 = intToBinary(pixel)
            if row < img1.shape[0] and col < img1.shape[1]:
                rgb1 = intToBinary(img1[row][col])
            else:
                rgb1 = intToBinary(n.array((0, 0, 0)))
            tup = mergeRGB(rgb1, rgb2)
            img2[row][col] = binaryToInt(tup)


def unmerge(img):
    row = -1
    col = -1
    for i in img:
        row += 1
        col = -1
        for pixel in i:
            col += 1
            r, g, b = intToBinary(pixel)
            rgb = ()

    print()


def main():
    # merge image1 to image2
    image1 = cv2.imread('waterfall2.png', 1)
    image2 = cv2.imread('sunset2.png', 1)
    cv2.imwrite('mergedScratch.png', image2)
    image2_copy = cv2.imread('mergedScratch.png', 1)
    # x=0
    # for i in image1:
    #     for pixel in i:
    #         x+=1
    #         print("For loop: ",pixel)
    #         if x==10:
    #             break
    #     if x==10:
    #         break
    # print("Normal 0,0: ",image1[0][0])
    # print("Normal 0,10: ",image1[0][10])
    # print(image1.shape) # 200,300,3
    # print(image2.shape) # 384,600,3

    merge(image1, image2_copy)

    # unmerge(image2_copy)


main()
