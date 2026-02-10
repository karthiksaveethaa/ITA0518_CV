import cv2
import numpy as np

p=r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg"
img=cv2.imread(p)
h,w=img.shape[:2]
M=np.float32([[0,-1,w],[1,0,0]])
out=cv2.warpAffine(img,M,(w,h))

cv2.imwrite("q12.jpg",out)
cv2.imshow("Output",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
