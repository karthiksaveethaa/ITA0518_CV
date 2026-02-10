import cv2

p=r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg"
img=cv2.imread(p)

roi=img[50:250,50:250]
img[300:500,300:500]=roi

cv2.imwrite("q18.jpg",img)
cv2.imshow("EXP18",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
