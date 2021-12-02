import imageQualityMeasure as iqm
import cv2
import numpy as np
import random
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')


def save(img, robustness):
    url = desktop + robustness + ".png"
    cv2.imwrite(url, img)


def cropping(c, s):
    print('\n----CROPPING----\n')
    #p = float(input('Enter the % to crop: '))
    p = 10
    row = int(c.shape[0]*(1-p/100))
    col = int(c.shape[1]*(1-p/100))
    s = s[0:row, 0:col]
    c = c[0:s.shape[0], 0:s.shape[1]]
    iqm.qualityMeasures(c, s)
    save(s, 'cropping')


def rotate(c, s):
    print('\n----ROTATING 180°----\n')
    s = cv2.rotate(s, cv2.ROTATE_180)
    iqm.qualityMeasures(c, s)
    save(s, 'rotate')


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
    save(out, 'gaussianNoise')


def poissonNoise(c, s):
    print('\n----AFTER ADDING POISSON NOISE----')
    imagea = s.astype(float)
    poissonNoise = np.random.poisson(imagea).astype(float)
    noisyImage = imagea + poissonNoise
    iqm.qualityMeasures(c, noisyImage)
    save(noisyImage, 'poissonNoise')


def speckleNoise(c, s):
    print('\n----AFTER ADDING SPECKLE NOISE----')
    gauss = np.random.normal(0, 1, s.size)
    gauss = gauss.reshape(s.shape[0], s.shape[1], 3).astype('uint8')
    noise = s + s * gauss
    iqm.qualityMeasures(c, noise)
    save(noise, 'speckleNoise')


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
    save(out, 'saltAndPepperNoise')


def medianFilter(c, s):
    print('\n----MEDIAN FILTER----\n')
    median = cv2.medianBlur(s, 5)
    iqm.qualityMeasures(c, median)
    save(median, 'medianFilter')


def averageFilter(c, s):
    print('\n----MEAN FILTER----\n')
    avg = cv2.blur(s, (6, 6))
    iqm.qualityMeasures(c, avg)
    save(avg, 'averageFilter')


def sharpening(c, s):
    print('\n----SHARPENING----\n')
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharp = cv2.filter2D(src=s, ddepth=-1, kernel=kernel)
    iqm.qualityMeasures(c, sharp)
    save(sharp, 'sharpening')


def histogramEqualization(c, s):
    print('\n----HISTOGRAM EQUALIZATION----\n')
    r, g, b = cv2.split(s)
    r_hist = cv2.equalizeHist(r)
    g_hist = cv2.equalizeHist(g)
    b_hist = cv2.equalizeHist(b)
    hist = cv2.merge((r_hist, g_hist, b_hist))
    iqm.qualityMeasures(c, hist)
    save(hist, 'histogramEqualization')


def main():
    cover = desktop + input('Cover image name with extension: ')
    stego = desktop + input('Stego imgae name with extension: ')

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
    medianFilter(coverImage, stegoImage)
    averageFilter(coverImage, stegoImage)
    sharpening(coverImage, stegoImage)
    histogramEqualization(coverImage, stegoImage)


main()
