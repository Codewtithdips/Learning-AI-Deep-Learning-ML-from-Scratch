import cv2

# Open input video (or webcam)
cap = cv2.VideoCapture("ssvid.net--lalala_1080pFHR.mp4")

# Get video properties (needed for VideoWriter)
frame_width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps          = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
# 'XVID' is common, output filename is 'output.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Example processing: draw text on frame
    cv2.putText(frame, "Processing...", (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Write the frame to output file
    out.write(frame)

    # Show the processed frame
    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
