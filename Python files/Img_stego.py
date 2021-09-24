from PIL import Image
import cv2
image1=Image.open(r'D:\Coding\DWMS project\img and txt stego\Steganography\New\content\waterfall2.jpg')
image2=Image.open(r'D:\Coding\DWMS project\img and txt stego\Steganography\New\content\sunset2.jpg')
#image1 = cv2.imread(r'D:\Coding\DWMS project\img and txt stego\Steganography\New\content\waterfall2.jpg', 1)
#image2 = cv2.imread(r'D:\Coding\DWMS project\img and txt stego\Steganography\New\content\sunset2.jpg', 1)
# image1 = Image.open('D:\Coding\DWMS project\img and txt stego\Steganography\New\content\sunset2.jpg')
# image2 = Image.open('D:\Coding\DWMS project\img and txt stego\Steganography\New\content\waterfall2.jpg')
print("over")

def int2bin(rgb):
    
    #Will convert RGB pixel values from integer to binary
    #INPUT: An integer tuple (e.g. (220, 110, 96))
    #OUTPUT: A string tuple (e.g. ("00101010", "11101011", "00010110"))
    
    r, g, b = rgb
    return ('{0:08b}'.format(r),
            '{0:08b}'.format(g),
            '{0:08b}'.format(b))
    #Return converted r,g,b binary values separately..

def bin2int(rgb):
    
    #Will convert RGB pixel values from binary to integer.
    #Reverse of the first part.
  
    r, g, b = rgb
    return (int(r, 2),
            int(g, 2),
            int(b, 2))
    #return converted r,g,b integer values separately
""" checking if the functions are working or not
r,g,b=int2bin((225,6,7))
print(r)
print(r[:4])
print(g)
print(b)
print(bin2int(('11100001', '00000110', '00000111')))
"""
def merge2rgb(rgb1,rgb2):
    
    #Will merge two RGB pixels using 4 least significant bits.
    #INPUT: A string tuple ( ("00101010", "11101011", "00010110")),another string tuple (e.g. ("00101010", "11101011", "00010110"))
    #OUTPUT: An integer tuple with the two RGB values merged
    #Will be merging the first four digits of first image and first four digits of 2nd image(i.e to be merged) as last four digits..
    

    r1,g1,b1=rgb1
    r2,g2,b2=rgb2

    return (r1[:4]+r2[:4],
             g1[:4]+g2[:4],
             b1[:4]+b2[:4]
          )

def merge2img(img1,img2):
  # The First image will be merged into the second image.


  image1=img1
  image2=img2
  #print('rahul')
  
  # Condition for merging
  if(image1.size[0]>image2.size[0] or image1.size[1]>image2.size[1]):
    print("Cannot merge as the size of 1st Image is greater than size of 2nd Image")
    return
  # Getting the pixel map of the two images

  pixel_tuple1 = image1.load()
  pixel_tuple2 = image2.load()

  #print(pixel_tuple1)
  #print(pixel_tuple2)

  # The new image that will be created.
  new_image = Image.new(image2.mode, image2.size) # Setting the size of Image 2 as Image 1 will be merged to Image 2.
  pixels_new = new_image.load()

  for row in range(image2.size[0]):
    for col in range(image2.size[1]):

        rgb1 = int2bin(pixel_tuple2[row, col])

        # Using a black pixel as default
        rgb2 = int2bin((0, 0, 0))

        # Converting the pixels of image 1 if condition is satisfied

        if(row <image1.size[0] and col< image1.size[1]):
          rgb2= int2bin(pixel_tuple1[row,col])


        merge_rgb= merge2rgb(rgb1,rgb2)

        pixels_new[row,col] = bin2int(merge_rgb) 

  #print('rahul')
  new_image.convert('RGB').save('merged1.jpg')
    
  return new_image   

merge2img(image1,image2) 

def unmerge(path):

    img=Image.open(path)

    # Loading the pixel map
    pixel_map = img.load()

    new_image = Image.new(img.mode, img.size)
    pixels_new = new_image.load()

    # Tuple used to store the image original size
    original_size = img.size

    for row in range(img.size[0]):
        for col in range(img.size[1]):
            # Get the RGB (as a string tuple) from the current pixel
            r, g, b = int2bin(pixel_map[row, col])

            # Extract the last 4 bits (corresponding to the hidden image)
            # Concatenate 4 zero bits because we are working with 8 bit values
            rgb = (r[4:] + "0000",
                   g[4:] + "0000",
                   b[4:] + "0000")

            # Convert it to an integer tuple
            pixels_new[row, col] = bin2int(rgb)

            # If this is a 'valid' position, store it
            # as the last valid position
            if pixels_new[row, col] != (0, 0, 0):
                original_size = (row + 1, col + 1)

    # Crop the image based on the 'valid' pixels
    new_image = new_image.crop((0, 0, original_size[0], original_size[1]))

    new_image.save('unmerged1.png')
    
    return new_image

unmerge('D:\Coding\DWMS project\img and txt stego\merged1.jpg')

def merge2rgb2(rgb1, rgb2):
    
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    rgb = (r1[:6] + r2[:2],
           g1[:6] + g2[:2],
           b1[:6] + b2[:2])
    return rgb

def merge2img2(img1, img2):

    image1=img1
    image2=img2
    #print('rahul')
  
    # Condition for merging
    if(image1.size[0]>image2.size[0] or image1.size[1]>image2.size[1]):
       print("Cannot merge as the size of 1st Image is greater than size of 2nd Image")
       return
  
  # Getting the pixel map of the two images
    pixel_tuple1 = image1.load()
    pixel_tuple2 = image2.load()

    #print(pixel_tuple1)
    #print(pixel_tuple2)

    # The new image that will be created.
    new_image = Image.new(image2.mode, image2.size) # Setting the size of Image 2 as Image 1 will be merged to Image 2.
    pixels_new = new_image.load()

    for row in range(image2.size[0]):
      for col in range(image2.size[1]):

        rgb1 = int2bin(pixel_tuple2[row, col])

        # Using a black pixel as default
        rgb2 = int2bin((0, 0, 0))

        # Converting the pixels of image 1 if condition is satisfied

        if(row <image1.size[0] and col< image1.size[1]):
          rgb2= int2bin(pixel_tuple1[row,col])

        merge_rgb= merge2rgb2(rgb1,rgb2)

        pixels_new[row,col] = bin2int(merge_rgb) 

    #print('rahul')
    new_image.convert('RGB').save('merged2.jpg')
    
    return new_image

def unmerge2(img):
    
    pixel_map = img.load()

    new_image = Image.new(img.mode, img.size)
    pixels_new = new_image.load()

    
    original_size = img.size

    for row in range(img.size[0]):
        for col in range(img.size[1]):
            r, g, b = int2bin(pixel_map[row, col])

            # Extracting the last 6 bits (corresponding to the hidden image) and adding zeroes to increase the brightness.
            
            rgb = (r[6:] + "000000",
                   g[6:] + "000000",
                   b[6:] + "000000")

            # Convert it to an integer tuple
            pixels_new[row, col] = bin2int(rgb)

           #If this is a 'valid' position, store it as a last valid option
            if pixels_new[row, col] != (0, 0, 0):
                original_size = (row + 1, col + 1)

    # Crop the image based on the 'valid' pixels
    new_image = new_image.crop((0, 0, original_size[0], original_size[1]))
    new_image.convert('RGB').save('unmerged2.jpg')
    return new_image

merged_image2 = merge2img2(image1,image2)
unmerged_image2 = unmerge2(merged_image2)
