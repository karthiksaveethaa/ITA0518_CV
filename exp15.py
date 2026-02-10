import cv2
import numpy as np

p=r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg"
img=cv2.imread(p)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

dst=cv2.cornerHarris(gray,2,3,0.04)
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imwrite("q15.jpg",img)
cv2.imshow("EXP15",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
