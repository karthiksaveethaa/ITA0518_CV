import cv2
import numpy as np

p=r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg"
img=cv2.imread(p,0)

sx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sy=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

sobel=cv2.magnitude(sx,sy)

cv2.imwrite("q16.jpg",sobel)
cv2.imshow("EXP16",sobel.astype("uint8"))
cv2.waitKey(0)
cv2.destroyAllWindows()
