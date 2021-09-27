import cv2
import numpy as np

def xor(a,b):
    if(a==b):
        return '0'
    return '1'

def message2binary(message):
    if type(message) == np.ndarray:  # for array (pixel)
        result = [format(i, "08b") for i in message]
        return result

    result = ''.join([format(ord(i), "08b") for i in message]) # for string (data)
    return result

def encode_data(img):
    #data = input("Enter the data to be Encoded:")
    data='qbsdakdsa'
    #filename = input("Enter the name of the New Image after Encoding(with extension):")
    filename='file.png'
    no_bytes = (img.shape[0] * img.shape[1] * 3) // 8 

    #print("Maximum bytes to encode:", no_bytes)
    if(len(data) > no_bytes):
        print("Need Bigger Image or give Less Data !!")
        quit()

    data += '*****'
    data_binary = message2binary(data)
    #print(data_binary)
    data_len = len(data_binary)
    #print("The Length of Binary data", data_len)

    data_index = 0
    for i in img:
        for pixel in i:
            r, g, b = message2binary(pixel)

            if data_index < data_len:
                pixel[0] = int(r[:-1] + xor(data_binary[data_index], r[-2]), 2)
                data_index += 1

                if data_index < data_len:
                    pixel[1] = int(g[:-1] + xor(data_binary[data_index],g[-2]), 2)
                    data_index += 1
    
                    if data_index < data_len:
                        pixel[2] = int(b[:-1] + xor(data_binary[data_index],b[-2]), 2)
                        data_index += 1
                    else:
                        break
                else:
                    break
            else:
                 break
        if data_index >= data_len:
                break

    cv2.imwrite(filename, img) 
    print("Encoded the data successfully and the image is successfully saved as ", filename)

def decode_data(img):
    binary_data = ""
    for i in img:
        for pixel in i:
            r, g, b = message2binary(pixel)
            binary_data += xor(r[-1],r[-2])
            binary_data += xor(g[-1],g[-2])
            binary_data += xor(b[-1],b[-2])

    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "*****":
            #print("***** reached")
            break
    print("The Encoded data was :--", decoded_data[:-5])

def main():
   print()
   image = cv2.imread('download2.png', 1)
   encode_data(image)
   image1 = cv2.imread('file.png')
   decode_data(image1)
   print()
main()
