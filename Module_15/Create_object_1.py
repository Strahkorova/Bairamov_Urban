# -*- coding: utf8 -*-
import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')

#RGB - стандарт
#BGR - формат в OpenCV
#photo[100:150, 200:250] = 119, 201, 105

cv2.rectangle(photo, (50, 70), (100, 100), (119, 201, 105), thickness=1)

cv2.putText(photo, 'Urban', (100, 150), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 100, (119, 201, 105), thickness=2)

cv2.imshow('Photo', photo)
cv2.waitKey(0)