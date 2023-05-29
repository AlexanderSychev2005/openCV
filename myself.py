import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')

# RGB - standard
# BGR - format in OpenCV
# photo[100:150, 200:280] = 255, 100, 100

cv2.rectangle(photo, (50, 70), (100, 100), (121, 168, 50), thickness=cv2.FILLED)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2),(121, 168, 50), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (121, 168, 50), thickness=1)

cv2.putText(photo, 'Studying', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
