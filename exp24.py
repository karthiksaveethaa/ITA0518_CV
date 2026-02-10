import cv2, numpy as np

p=r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg"
img=cv2.imread(p,0)

k=np.ones((9,9),np.uint8)
out=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,k)

cv2.imshow("BlackHat",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
