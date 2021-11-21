import imageQualityMeasure as iqm
import cv2
from PIL import Image

def cropping(c,s):
    print('\nCROPPING \n')
    p=float(input('Enter the % to crop: '))
    row=int(c.shape[0]*(1-p/100))
    col=int(c.shape[1]*(1-p/100))
    s=s[0:row,0:col]
    c=c[0:s.shape[0],0:s.shape[1]]
    iqm.qualityMeasures(c,s)



def main():
    matrix=[[]]
    cover = 'Images\\' + input('Cover image name with extension: ')
    stego = 'Images\\' + input('Stego imgae name with extension: ')

    coverImage = cv2.imread(cover, 1)
    stegoImage = cv2.imread(stego, 1)

    # c = np.array([[[20, 30, 10], [10, 20, 30], [10, 40, 30]],
    #  [[70, 10, 80], [30, 90, 40], [30, 60, 50]],
    #  [[50, 50, 50], [10, 50, 90], [30, 60, 10]]])

    # s = np.array([[[21, 29, 11], [10, 21, 29], [10, 40, 30]],
    #  [[71, 10, 79], [30, 91, 39], [31, 61, 51]],
    #  [[50, 50, 50], [10, 51, 90], [31, 60, 9]]])
    print('\n\nImage Quality Measures without any attacks: \n')
    iqm.qualityMeasures(coverImage,stegoImage)
    
    print('\nQuality meaasures after the following robustness attacks: \n')
    cropping(coverImage,stegoImage)
main()