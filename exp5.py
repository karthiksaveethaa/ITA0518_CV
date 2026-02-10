import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg")
b,g,r = cv2.split(img)
hb = cv2.calcHist([b],[0],None,[256],[0,256])
hg = cv2.calcHist([g],[0],None,[256],[0,256])
hr = cv2.calcHist([r],[0],None,[256],[0,256])
print("Blue Histogram:",hb.flatten())
print("Green Histogram:",hg.flatten())
print("Red Histogram:",hr.flatten())
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()