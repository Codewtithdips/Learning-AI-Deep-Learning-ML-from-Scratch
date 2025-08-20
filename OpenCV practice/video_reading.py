import cv2

# Open video file
cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()  # frame = one image from the video
    
    if not ret:
        break  # No more frames
    
    cv2.imshow("Video Frame", frame)  # Show the frame
    
    if cv2.waitKey(25) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
