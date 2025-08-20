import cv2
import numpy as np

# Create a pure red image in BGR
red_img = np.zeros((300, 300, 3), dtype="uint8")
red_img[:] = (0, 0, 255)  # BGR (Blue=0, Green=0, Red=255)

cv2.imshow("Red in OpenCV", red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
