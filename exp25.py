import cv2

p=r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg"
img=cv2.imread(p,0)

orb=cv2.ORB_create()
kp,des=orb.detectAndCompute(img,None)

out=cv2.drawKeypoints(img,kp,None)

cv2.imshow("Watch Detection",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
