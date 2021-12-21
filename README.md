# Image-Steganography
Digital Watermarking and Steganography 
The program uses LSB technique to watermark. Information is not stored directly like simple LSB, it uses different algorithms for each steganography.
You can insert a secret text or a secret image inside a cover image of your choice. There is no visible change in the cover image yet your data is saved in it. 
You can also extract the data embedded if you have the right file. Extracting information works only for this specific algorithm, it is subjective to other watermaking techniques.  

#HOW TO RUN THE CODE: 

TO ENCODE AND DECODE 

1. Run the app.py file.
2. Open the website and navigate there. 

Note: Image embedding might take a few seconds to process depending on the system. 

TO CHECK FOR ROBUSTNESS 

1. Run the 'robustnessAttacks.py' file in the 'Python files' folder. 
2. Enter the cover and stego image name. (make sure the images are on desktop)
3. Images after applying robustness will be saved on desktop. 


#ALGORITHM FOR TEXT EMBEDDING:

1. Take input of text that is to be hidden and create a function to convert the text to binary format.
2. For the conversion of the text to binary digits , 8 bit representation of the text is taken into account.
3. Input the image in any file format where you wish to embed your message.
4. Perform the XOR condition between the 2nd LSB of each pixel (cover image) and bits of message.
5. Replace the resultant with the LSB of the cover image.
6. Repeat step 4 and 5 for every pixel (red green blue) of the cover image.
7. And the data is embedded on the cover image.
8. For retrieving the message from the embedded image, perform the XOR condition between the LSB and 2nd LSB of the image. The resultant is the bit of secret message encoded.
9. Repeat step 8 for every pixel until the message is encoded. 

#ALGORITHM FOR IMAGE EMBEDDING:

1. Input original image in any format.
2. Input watermark in any File format.
3. Resize the watermark according to original image.
4. Merge the first 6 bits of the original image and first 2 bits of the watermark image.
5. Get watermarked image.
6. To decode the embedded image from the watermark image, take the last two bits of the watermarked image and add six zeros to it. (So that it will be a 8 bit pixel and adding zeros will increase the brightness of the image).   
