import cv2
import numpy as np

# Create a blank white image (500x500, 3 color channels)
img = np.ones((500, 500, 3), dtype="uint8") * 255

# 1. Draw a line (start_point, end_point, color, thickness)
cv2.line(img, (50, 50), (450, 50), (255, 0, 0), 3)  # Blue line

# 2. Draw a rectangle (top_left, bottom_right, color, thickness)
cv2.rectangle(img, (50, 100), (200, 300), (0, 255, 0), 3)  # Green rectangle

# 3. Draw a circle (center, radius, color, thickness)
cv2.circle(img, (350, 200), 80, (0, 0, 255), -1)  # Solid red circle

# 4. Put text (image, text, bottom-left-corner, font, fontScale, color, thickness)
cv2.putText(img, "Hello OpenCV!", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Show the image
cv2.imshow("Drawing Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
