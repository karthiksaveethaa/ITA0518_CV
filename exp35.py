import cv2

text = input("Enter text: ")

img = cv2.imread(r"C:\users\administrator\Pictures\photos\WhatsApp Image 2025-06-15 at 21.38.44_75b4eefb.jpg")

cv2.putText(img, text, (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Text Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()