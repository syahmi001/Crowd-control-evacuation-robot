import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("/home/pi/Downloads/template4.jpg",0)
img2 = img.copy()
template1 = cv.imread("/home/pi/Downloads/x.jpg",0)
template2 = cv.imread("/home/pi/Downloads/y.jpg",0)
w1, h1 = template1.shape[::-1]
w2, h2 = template2.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res1 = cv.matchTemplate(img,template1,method)
    res2 = cv.matchTemplate(img,template2,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res1)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res2)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w1, top_left[1] + h1)
    bottom_right = (top_left[0] + w2, top_left[1] + h2)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    
    plt.subplot(121),plt.imshow(res1,cmap = 'gray')
    plt.subplot(121),plt.imshow(res2,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
