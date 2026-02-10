import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow("Normal",frame)
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow("Slow Motion",frame)
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow("Fast Motion",frame)
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()