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


def UIQI(c, s):
    mu_c = c.mean()
    mu_s = s.mean()
    sd_c = np.std(c)
    sd_s = np.std(s)
    cor = np.correlate(np.ndarray.flatten(c), np.ndarray.flatten(s))
    Q = (4*cor*mu_c*mu_s)/((sd_c**2 + sd_s**2)*(mu_c**2 + mu_s**2))
    Q = Q[0]
    Q = to3decimal(Q)
    return Q


def capacity(c,s):
    cap = (c.shape[0]*c.shape[1]*3)//8
    print('Total embedding capacity of cover image is', cap, 'characters (8 bit)\n')


def qualityMeasures(c,s):
    print()
    capacity(c,s)
    print('Mean square error (MSE):', MSE(c,s))
    print('Root Mean square error (RMSE):',RMSE(c, s))
    print('Signal-to-noise ratio (SNR): ', SNR(c, s))
    print('Peak signal-to-noise ratio (PSNR)', PSNR(c, s))
    print('Average Difference (AD):', AD(c, s))
    print('Normalized cross correlation (NCC):', NCC(c, s))
    print('Image Fidelity (IF):', IF(c, s))
    print('Structural Content (SC):', SC(c, s))
    print('Normalised Absolute Error (NAE):', NAE(c, s))
    print('Structural similarity index measure (SSIM):', SSIM(c, s))
    print('Structural dissimilarity index measure (DSSIM):', DSSIM(c, s))
    print('Universal Image Quality Index (UIQI):', UIQI(c, s))
    print()