import cv2
import numpy as np

p=r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg"
img=cv2.imread(p)
h,w=img.shape[:2]

pts1=np.float32([[0,0],[w,0],[0,h],[w,h]])
pts2=np.float32([[40,40],[w-60,20],[60,h-40],[w-40,h-20]])

M=cv2.getPerspectiveTransform(pts1,pts2)
out=cv2.warpPerspective(img,M,(w,h))

cv2.imwrite("q14.jpg",out)
cv2.imshow("EXP14",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
