import cv2

p=r"C:\Users\Administrator\Pictures\WhatsApp Image 2026-02-07 at 9.30.28 AM.jpeg"
img=cv2.imread(p)

wm=img.copy()
cv2.putText(wm,"WATERMARK",(50,120),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)

out=cv2.addWeighted(img,0.8,wm,0.2,0)

cv2.imwrite("q17.jpg",out)
cv2.imshow("EXP17",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
