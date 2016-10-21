import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('images/route.jpg', 0)

cv2.imshow('image sans filtre',img)

ret,thresh = cv2.threshold(img, 230, 255, 0)


image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image avec contour',image)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()