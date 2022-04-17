"""import X just imports the entire module (read: "runs the module"), and assigns it a name in the local scope.
You can also do from x import something, which imports just the something into the local namespace, not everything in x."""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

file_path= 'r C:\Projects\Projects\TextExtraction'

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img
file_path = '.\img1.jpg'
img = cv_imread(file_path)
print(img)

imgbgr=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(imgbgr)
#pixel values greater than the threshold value are assigned the maximum value specified in the function. Otherwise, they are assigned 0.
ret, thresh1 = cv2.threshold(imgbgr, 120, 255, cv2.THRESH_BINARY)

#inverse of the cv2.THRESH_BINARY. If the pixel value is greater than the threshold value, it is assigned 0, else the maximum value
ret, thresh2 = cv2.threshold(imgbgr, 120, 255, cv2.THRESH_BINARY_INV)

#If the pixel value is greater than the threshold, it is assigned the threshold value. Otherwise, the value remains the same.
ret, thresh3 = cv2.threshold(imgbgr, 120, 255, cv2.THRESH_TRUNC)

#all the pixels having values greater than the threshold value stay the same, and the remaining ones become 0
ret, thresh4 = cv2.threshold(imgbgr, 120, 255, cv2.THRESH_TOZERO)

#the inverse of the cv2.THRESH_TOZERO
ret, thresh5 = cv2.threshold(imgbgr, 120, 255, cv2.THRESH_TOZERO_INV)

#plt.imshow just finishes drawing a picture instead of printing it. If you want to print the picture, you just need to add plt.show.

print("Thesrholding1")
plt.imshow( thresh1)
plt.show()
print("Thesrholding2")

plt.imshow(thresh2)
plt.show()
print("Thesrholding3")
plt.imshow(thresh3)
plt.show()
print("Thesrholding4")
plt.imshow(thresh4)
plt.show()
print("Thesrholding5")
plt.imshow(thresh5)
plt.show()

pytesseract.pytesseract.tesseract_cmd = r"C:/Users/priya.ak.singh/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18,18))
print(kernel)

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, kernel, iterations = 1)
print(dilation)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


img2= imgbgr.copy()

# A text file is created and flushed
file = open("detected_text.txt", "w+")
file.write("")
file.close()    

# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
     
    # Drawing a rectangle on copied image
    rect = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
    # Cropping the text block for giving input to OCR
    cropped = img2[y:y + h, x:x + w]
     
    # Open the file in append mode
    file = open("detected_text.txt", "a")
     
    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)
     
    # Appending the text into file
    file.write(text)
    file.write("\n")
     
    # Close the file
    file.close

                                                
