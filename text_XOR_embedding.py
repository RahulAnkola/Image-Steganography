import cv2
import numpy as n
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')

def xor(a, b):
    if a == b:
        return '0'
    return '1'


def toBinary(msg):
    if type(msg) == n.ndarray:  # for numpy array
        binary = [format(i, "08b") for i in msg]
        return binary
    binary = ''.join([format(ord(i), "08b") for i in msg])  # for string
    return binary


def encodeData(img, data):
    data += '***'
    capacity = (img.shape[0]*img.shape[1]*3)//8

    if(len(data) > capacity):
        print("Need Bigger Image or give Less Data !!")
        quit()

    binaryData = toBinary(data)
    dataLen = len(binaryData)
    index = 0

    for i in img:
        for pixel in i:
            r, g, b = toBinary(pixel)

            if index < dataLen:
                pixel[0] = int(r[:-1] + xor(binaryData[index], r[-2]), 2)
                index += 1

                if index < dataLen:
                    pixel[1] = int(g[:-1] + xor(binaryData[index], g[-2]), 2)
                    index += 1

                    if index < dataLen:
                        pixel[2] = int(
                            b[:-1] + xor(binaryData[index], b[-2]), 2)
                        index += 1
                    else:
                        break
                else:
                    break
            else:
                break

        if index >= dataLen:
            break
    stegoImage = desktop + 'TextStego.png'
    cv2.imwrite(stegoImage, img)
    print("Data encoded successfully")


def decodeData(img):
    binaryData = ''
    # print(img)
    for i in img:
        for pixel in i:
            r, g, b = toBinary(pixel)
            binaryData += xor(r[-1], r[-2])
            binaryData += xor(g[-1], g[-2])
            binaryData += xor(b[-1], b[-2])
    msgBinary = []
    decoded = ''
    for i in range(0, len(binaryData), 8):
        msgBinary.append(binaryData[i:i+8])
        decoded += chr(int(msgBinary[i//8], 2))
        if decoded[-3:] == '***':
            #print("*** reached")
            break
    print("\nEncoded data:", decoded[:-3])
    return decoded[:-3]
