import numpy as np
import cv2

img = cv2.imread('images/tests/3pots.jpg', 1)

cv2.imshow('3 pots sans traitement', img)


# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_green = np.array([34,50,50])
upper_green = np.array([86,255,255])

# Threshold the HSV image to get only green colors
mask = cv2.inRange(hsv, lower_green, upper_green)
cv2.imshow('Mask de vert', mask)

masked_data = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("masked", masked_data)
cv2.imwrite( "images/tests/mask.jpg", masked_data )


#ret,thresh = cv2.threshold(img, 230, 255, 0)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image avec contour',image)

k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.destroyAllWindows()