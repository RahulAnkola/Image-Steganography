# Image-Steganography
Digital Watermarking and Steganography 
The program uses LSB technique to watermark. Information is not stored directly like simple LSB, it uses different algorithms for each steganography.
You can insert a secret text or a secret image inside a cover image of your choice. There is no visible change in the cover image yet your data is saved in it. 
You can also extract the data embedded if you have the right file. Extracting information works only for this specific algorithm, it is subjective to other watermaking techniques.  
#PACKAGES REQUIRED 
1. OpenCV
2. Flask
3. Numpy
 
#HOW TO RUN THE CODE: 

TO ENCODE AND DECODE 

1. Run the app.py file.
2. Open the website and navigate there. 

Note: Image embedding might take a few seconds to process depending on the system. 

TO CHECK FOR ROBUSTNESS 

1. Run the 'robustnessAttacks.py' file in the 'Python files' folder. 
2. Enter the cover and stego image name. (make sure the images are on desktop)
3. Images after applying robustness will be saved on desktop. 

Refer the document or ppt for more details. (Includes algorithm to encode and decode)
