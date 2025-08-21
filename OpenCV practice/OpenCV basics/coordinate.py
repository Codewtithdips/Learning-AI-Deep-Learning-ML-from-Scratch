import cv2
import numpy as np

# Create a blank black image (500x500)
img = 255 * np.ones((500, 500, 3), dtype="uint8")

# Draw a circle at (100, 200)
cv2.circle(img, (100, 200), 10, (0, 0, 255), -1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
