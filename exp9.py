import cv2

img = cv2.imread(r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg")
small = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
big = cv2.resize(img,(0,0),fx=2,fy=2)
cv2.imshow("Original",img)
cv2.imshow("Smaller",small)
cv2.imshow("Bigger",big)
cv2.waitKey(0)
cv2.destroyAllWindows()