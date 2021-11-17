import cv2
import numpy as np
import math as math


def to3decimal(x):
    return float("{0:.3f}".format(x))


def MSE(c, s):
    mse = (np.sum((c-s)**2))/(c.shape[0]*c.shape[1])
    mse = to3decimal(mse)
    return mse


def RMSE(c, s):
    rmse = math.sqrt(MSE(c, s))
    rmse = to3decimal(rmse)
    return rmse


def SNR(c, s):
    x = np.sum(c**2)/np.sum((c-s)**2)
    snr = 10*math.log(x, 10)
    snr = to3decimal(snr)
    return snr


def PSNR(c, s):
    x = 255*255/MSE(c, s)
    psnr = 10*math.log(x, 10)
    psnr = to3decimal(psnr)
    return psnr


def AD(c, s):
    ad = np.sum(c-s)/(c.shape[0]*c.shape[1])
    ad = to3decimal(ad)
    return ad


def NCC(c, s):
    ncc = np.sum((c*s)**2)/np.sum(c**2)
    ncc = to3decimal(ncc)
    return ncc


def IF(c, s):
    imf = 1-NCC(c, s)
    imf = to3decimal(imf)
    return imf


def SC(c, s):
    sc = np.sum(s**2)/np.sum(c**2)
    sc = to3decimal(sc)
    return sc


def NAE(c, s):
    nae = np.sum(abs(c-s))/np.sum(c)
    nae = to3decimal(nae)
    return nae


def SSIM(c, s):
    mu_c = c.mean()
    mu_s = s.mean()
    sd_c = np.std(c)
    sd_s = np.std(s)
    cor = np.correlate(np.ndarray.flatten(c), np.ndarray.flatten(s))
    c1 = (0.01*255)**2
    c2 = (0.03*255)**2
    ssim = ((2*mu_c*mu_s + c1)*(2*cor + c2)) / \
        ((mu_c**2 + mu_s**2 + c1)*(sd_c**2 + sd_s**2 + c2))
    ssim = ssim[0]
    ssim = to3decimal(ssim)
    return ssim


def DSSIM(c, s):
    dssim = (1-SSIM(c, s))/2
    dssim = to3decimal(dssim)
    return dssim


def capacity(c):
    cap = (c.shape[0]*c.shape[1]*3)//8
    print('Embedding capacity of cover image is', cap, 'characters (8 bit)\n')


def main():
    c = input('Cover image name with extension: ')
    s = input('Stego imgae name with extension: ')
    c = 'Images\\' + c
    s = 'Images\\' + s

    c = cv2.imread(c, 1)
    s = cv2.imread(s, 1)

    # c = np.array([[[20, 30, 10], [10, 20, 30], [10, 40, 30]],
    #  [[70, 10, 80], [30, 90, 40], [30, 60, 50]],
    #  [[50, 50, 50], [10, 50, 90], [30, 60, 10]]])

    # s = np.array([[[21, 29, 11], [10, 21, 29], [10, 40, 30]],
    #  [[71, 10, 79], [30, 91, 39], [31, 61, 51]],
    #  [[50, 50, 50], [10, 51, 90], [31, 60, 9]]])

    print()

    mse = MSE(c, s)
    rmse = RMSE(c, s)
    snr = SNR(c, s)
    psnr = PSNR(c, s)
    ad = AD(c, s)
    ncc = NCC(c, s)
    imf = IF(c, s)
    sc = SC(c, s)
    nae = NAE(c, s)
    ssim = SSIM(c, s)
    dssim = DSSIM(c, s)

    capacity(c)
    print('Mean square error (MSE):', mse)
    print('Root Mean square error (RMSE):', rmse)
    print('Signal-to-noise ratio (SNR): ', snr)
    print('Peak signal-to-noise ratio (PSNR)', psnr)
    print('Average Difference (AD):', ad)
    print('Normalized cross correlation (NCC):', ncc)
    print('Image Fidelity (IF):', imf)
    print('(SC):', sc)
    print('Normalised Absolute Error (NAE):', nae)
    print('Structural similarity index measure (SSIM):', ssim)
    print('Structural dissimilarity index measure (DSSIM):', dssim)

    print()


main()
