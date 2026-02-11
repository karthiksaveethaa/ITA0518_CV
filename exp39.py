import cv2

cap = cv2.VideoCapture(0)
frames = []

while True:
    ret, f = cap.read()
    if not ret:
        break

    cv2.imshow("Recording", f)
    frames.append(f)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

for f in frames[::-1]:
    cv2.imshow("Reverse Slow", f)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()