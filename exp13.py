import cv2
import numpy as np

p=r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg"
img=cv2.imread(p)
h,w=img.shape[:2]

pts1=np.float32([[0,0],[w-1,0],[0,h-1]])
pts2=np.float32([[50,50],[w-100,80],[80,h-50]])

M=cv2.getAffineTransform(pts1,pts2)
out=cv2.warpAffine(img,M,(w,h))

cv2.imwrite("q13.jpg",out)
cv2.imshow("EXP13",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
