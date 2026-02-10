import cv2

img = cv2.imread(r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(gray)
cv2.imshow("Original",gray)
cv2.imshow("Equalized",eq)
cv2.waitKey(0)
cv2.destroyAllWindows()