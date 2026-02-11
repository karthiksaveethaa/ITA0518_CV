import cv2
cap=cv2.VideoCapture(0)
frames=[]
while True:
    ret,f=cap.read()
    if not ret:
        break
    frames.append(f)
    cv2.imshow("Capture",f)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
for f in frames[::-1]:
    cv2.imshow("Reverse",f)
    if cv2.waitKey(30)==ord('q'):
        break
cv2.destroyAllWindows()