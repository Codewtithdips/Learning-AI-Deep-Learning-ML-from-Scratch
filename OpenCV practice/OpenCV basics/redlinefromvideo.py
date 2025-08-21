import cv2

# Load input video
cap = cv2.VideoCapture("ssvid.net--lalala_1080pFHR.mp4")

# Get video properties
frame_width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps          = int(cap.get(cv2.CAP_PROP_FPS))

# Define VideoWriter to save processed video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, fps, (frame_width, frame_height))

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1  # Keep track of frame number
    
    # Draw a red horizontal line across the middle
    mid_y = frame_height // 2
    cv2.line(frame, (0, mid_y), (frame_width, mid_y), (0, 0, 255), 3)
    
    # Overlay frame number text
    cv2.putText(frame, f"Frame: {frame_count}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Save processed frame
    out.write(frame)
    
    # Show the frame while processing
    cv2.imshow("Processed Video", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
