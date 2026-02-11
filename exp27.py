import cv2
face=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
img=cv2.imread(r"C:\users\administrator\Pictures\photos\WhatsApp Image 2025-06-15 at 21.38.44_75b4eefb.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
f=face.detectMultiScale(gray,1.3,5)
for(x,y,w,h) in f:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("Face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()