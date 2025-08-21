import cv2

# Open video file (or use 0 for webcam)
cap = cv2.VideoCapture("ssvid.net--lalala_1080pFHR.mp4")  

# Loop through frames
while True:
    ret, frame = cap.read()   # ret = True if frame read successfully, frame = the image
    
    if not ret:
        break   # no more frames, exit loop
    
    # Show the frame
    cv2.imshow("Video", frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
