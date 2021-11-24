import imageQualityMeasure as iqm
import cv2
import numpy as np
import random


def cropping(c, s):
    print('\n----CROPPING----\n')
    p = float(input('Enter the % to crop: '))
    row = int(c.shape[0]*(1-p/100))
    col = int(c.shape[1]*(1-p/100))
    s = s[0:row, 0:col]
    c = c[0:s.shape[0], 0:s.shape[1]]
    iqm.qualityMeasures(c, s)


def rotate(c, s):
    print('\n----ROTATING----\n')
    s = cv2.rotate(s, cv2.ROTATE_180)
    iqm.qualityMeasures(c, s)


def gaussianNoise(c, s):
    print('\n----AFTER ADDING GAUSSIAN NOISE----')
    mean = 0
    var = 0.01
    s = np.array(s/255, dtype=float)
    noise = np.random.normal(mean, var**0.5, s.shape)
    out = s+noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    iqm.qualityMeasures(c, out)


def poissonNoise(c, s):
    print('\n----AFTER ADDING POISSON NOISE----')
    imagea = s.astype(float)
    poissonNoise = np.random.poisson(imagea).astype(float)
    noisyImage = imagea + poissonNoise
    iqm.qualityMeasures(c, noisyImage)


def speckleNoise(c, s):
    print('\n----AFTER ADDING SPECKLE NOISE----')
    gauss = np.random.normal(0, 1, s.size)
    gauss = gauss.reshape(s.shape[0], s.shape[1], 3).astype('uint8')
    noise = s + s * gauss
    iqm.qualityMeasures(c, noise)


def saltAndPepperNoise(c, s):
    print('\n----AFTER ADDING SALT & PEPPER NOISE----\n')
    s_vs_p = 0.5
    amount = 0.04
    out = np.copy(s)

    num_salt = np.ceil(amount * s.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in s.shape]
    out[coords] = 1

    num_pepper = np.ceil(amount * s.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in s.shape]
    out[coords] = 0

    iqm.qualityMeasures(c, out)


def main():
    #    cover = 'Images\\' + input('Cover image name with extension: ')
    #    stego = 'Images\\' + input('Stego imgae name with extension: ')
    cover = 'Images\\sunset2.png'
    stego = 'Images\\merged.png'
    coverImage = cv2.imread(cover, 1)
    stegoImage = cv2.imread(stego, 1)

    print('\n\nImage Quality Measures without any attacks: \n')
    iqm.qualityMeasures(coverImage, stegoImage)

    print('\nQuality meaasures after the following robustness attacks: \n')
    cropping(coverImage, stegoImage)
    rotate(coverImage, stegoImage)
    gaussianNoise(coverImage, stegoImage)
    poissonNoise(coverImage, stegoImage)
    speckleNoise(coverImage, stegoImage)
    saltAndPepperNoise(coverImage, stegoImage)


main()
