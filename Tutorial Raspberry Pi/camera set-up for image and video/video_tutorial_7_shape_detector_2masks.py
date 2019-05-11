import cv2
import numpy as np
import imutils
from picamera.array import PiRGBArray
from picamera import PiCamera 

def nothing(x):
    pass

cv2.namedWindow("Trackbars")
 
cv2.createTrackbar("L-H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 66, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 134, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 243, 255, nothing)

font = cv2.FONT_HERSHEY_COMPLEX
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    lower_red = np.array([0, 66, 134])
    upper_red = np.array([180, 255, 243])

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5, 5), np.uint8)
    mask_red = cv2.erode(mask_red, kernel)

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((5, 5), np.uint8)
    mask_blue = cv2.erode(mask_blue, kernel)

     #Contours detection
    _, contours, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    _, contours, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #for cnt in contours:
        #area = cv2.contourArea(cnt)
        #approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        #x = approx.ravel()[0]
        #y = approx.ravel()[1]

        #if area > 1000:
            #cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)

            #if len(approx) == 3:
                #cv2.putText(image, "Triangle", (x, y), font, 1, (0, 0, 0))
            #elif len(approx) == 4:
                #cv2.putText(image, "Rectangle", (x, y), font, 1, (0, 0, 0))
            #elif 10 < len(approx) < 20:
                #cv2.putText(image, "Circle", (x, y), font, 1, (0, 0, 0))

    cv2.imshow("Image", image)
    cv2.imshow("Mask Red", mask_red)
    cv2.imshow("Mask Blue", mask_blue)

    key = cv2.waitKey(1)
    rawCapture.truncate(0)
    if key == ord("q"):
        break

cv2.destroyAllWindows()

    

