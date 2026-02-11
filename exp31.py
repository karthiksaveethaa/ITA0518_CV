import cv2
img=cv2.imread(r"C:\users\administrator\Pictures\photos\WhatsApp Image 2025-06-15 at 21.38.44_75b4eefb.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,th=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("Segmented",th)
cv2.waitKey(0)
cv2.destroyAllWindows()