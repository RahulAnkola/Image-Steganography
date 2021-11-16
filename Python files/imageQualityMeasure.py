import cv2
import numpy as np
import math as math


def MSE(c, s):
    mse = (np.sum((c-s)**2))/(c.shape[0]*c.shape[1])
    mse = float("{0:.3f}".format(mse))
    return mse


def RMSE(c, s):
    rmse = math.sqrt(MSE(c, s))
    rmse = float("{0:.3f}".format(rmse))
    return rmse


def SNR(c, s):
    x = np.sum(c**2)/np.sum((c-s)**2)
    snr = 10*math.log(x, 10)
    snr = float("{0:.3f}".format(snr))
    return snr


def PSNR(c, s):
    x = 255*255/MSE(c, s)
    psnr = 10*math.log(x, 10)
    return psnr


def AD(c, s):
    ad = np.sum(c-s)/(c.shape[0]*c.shape[1])
    ad= float("{0:.3f}".format(ad))
    return ad

def NCC(c,s):
    ncc=np.sum((c*s)**2)/np.sum(c**2)
    ncc=float("{0:.3f}".format(ncc))
    return ncc
def IF(c,s):
    imf=1-NCC(c,s)
    imf=float("{0:.3f}".format(imf))
    return imf


def main():
    #cover=input('Cover image name with extension: ')
    #stego=input('Stego imgae name with extension: ')
    #cover='Images\\' + cover
    #stego='Images\\' + stego
    #
    # coveri=cv2.imread(cover,1)
    #stegoi=cv2.imread(stego, 1)

    c = np.array([[[20, 30, 10], [10, 20, 30], [10, 40, 30]],
                 [[70, 10, 80], [30, 90, 40], [30, 60, 50]],
                 [[50, 50, 50], [10, 50, 90], [30, 60, 10]]])

    s = np.array([[[21, 29, 11], [10, 21, 29], [10, 40, 30]],
                 [[71, 10, 79], [30, 91, 39], [31, 61, 51]],
                 [[50, 50, 50], [10, 51, 90], [31, 60, 9]]])

    print()
    mse = MSE(c, s)
    rmse = RMSE(c, s)
    snr = SNR(c, s)
    psnr = PSNR(c, s)
    ad= AD(c,s)
    ncc=NCC(c,s)
    imf=IF(c,s)
    print('Mean square error (MSE):', mse)
    print('Root Mean square error (RMSE):', rmse)
    print('Signal-to-noise ratio (SNR): ', snr)
    print('Peak signal-to-noise ratio (PSNR)', psnr)
    print('Average Difference (AD):',ad)
    print('Normalized cross correlation (NCC):', ncc)
    print('Image Fidelity (IF):',imf)

    print()


main()
