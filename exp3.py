import cv2

img = cv2.imread(r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,200)
cv2.imshow("Original",img)
cv2.imshow("Canny Outline",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()