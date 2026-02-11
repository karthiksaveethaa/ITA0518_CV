import cv2
smile=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
img=cv2.imread(r"C:\users\administrator\Pictures\photos\WhatsApp Image 2025-06-15 at 21.38.44_75b4eefb.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
s=smile.detectMultiScale(gray,1.8,20)
for(x,y,w,h) in s:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
cv2.imshow("Smile",img)
cv2.waitKey(0)
cv2.destroyAllWindows()