import cv2

cap = cv2.VideoCapture("ssvid.net--lalala_1080pFHR.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("FPS:", fps)
print("Total Frames:", frame_count)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_index = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    print("Frame Index:", frame_index, "/", frame_count)

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
