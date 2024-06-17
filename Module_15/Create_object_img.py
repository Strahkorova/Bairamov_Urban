# -*- coding: utf8 -*-
import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')
photo[:] = 255, 112, 88

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 220, (255, 255, 255), thickness=4)

cv2.ellipse(photo, (250, 300), (80, 80), 0, 0, 180, (0, 255, 0), thickness=5)
cv2.ellipse(photo, (250, 300), (50, 50), 0, 0, 180, (0, 255, 0), thickness=5)

cv2.line(photo, (170, 300), (170, 200), (255, 0, 0), thickness=5)
cv2.line(photo, (200, 300), (200, 200), (255, 0, 0), thickness=5)
cv2.line(photo, (300, 300), (300, 200), (255, 0, 0), thickness=5)
cv2.line(photo, (330, 300), (330, 200), (255, 0, 0), thickness=5)

cv2.line(photo, (170, 200), (200, 200), (0, 0, 255), thickness=5)
cv2.line(photo, (300, 200), (330, 200), (0, 0, 255), thickness=5)

cv2.putText(photo, 'Urban', (200, 150), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)

cv2.imshow('Photo', photo)
cv2.waitKey(0)