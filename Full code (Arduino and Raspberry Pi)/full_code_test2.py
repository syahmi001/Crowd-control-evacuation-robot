from picamera.array import PiRGBArray
import serial
from picamera import PiCamera 
import time
import cv2
import numpy as np
import imutils

face_cascade = cv2.CascadeClassifier("/home/pi/Camera_test/haarcascade_frontalface_default.xml")

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
camera.framerate = 32
camera.rotation = 180
camera.start_recording("/home/pi/video1.h264")

rawCapture = PiRGBArray(camera, size=(640, 480))

try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
        hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        l_h = cv2.getTrackbarPos("L-H", "Trackbars")
        l_s = cv2.getTrackbarPos("L-S", "Trackbars")
        l_v = cv2.getTrackbarPos("L-V", "Trackbars")
        u_h = cv2.getTrackbarPos("U-H", "Trackbars")
        u_s = cv2.getTrackbarPos("U-S", "Trackbars")
        u_v = cv2.getTrackbarPos("U-V", "Trackbars")

        lower_red = np.array([0, 108, 110])
        upper_red = np.array([17, 255, 243])

        lower_green = np.array([48, 116, 71])
        upper_green = np.array([92, 255, 255])

        #lower_green = np.array([l_h, l_s, l_v])
        #upper_green = np.array([u_h, u_s, u_v])

        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        kernel = np.ones((5, 5), np.uint8)
        mask_red = cv2.erode(mask_red, kernel)

        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        kernel = np.ones((5, 5), np.uint8)
        mask_green = cv2.erode(mask_green, kernel)
        a = 0
        b = 0
        c = 0
        d = 0
        #e = 0

        
        #face detection
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
            cv2.putText(image, "Face detected!", (x, y), font, 1, (0, 0, 0))
            a = 1

            if a == 1:
                print("Initiating program")
                ser.write(str('1').encode())
                time.sleep(1)
            

        #Contours detection
        _, contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _, contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt_red in contours_red:
            area = cv2.contourArea(cnt_red)
            approx = cv2.approxPolyDP(cnt_red, 0.02*cv2.arcLength(cnt_red, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if area > 2500:
                cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)

                if len(approx) == 3:
                    cv2.putText(image, "Go Right", (x, y), font, 1, (0, 0, 0))
                    print("Red Triangle detected!")
                    b = 1

                #elif len(approx) == 4:
                    #cv2.putText(image, "Go left", (x, y), font, 1, (0, 0, 0))
                    #print("Red Rectangle detected!")
                    #e = 1

                if b == 1:
                    print("Going right")
                    ser.write(str('2').encode())
                    time.sleep(1)
            
        for cnt_green in contours_green:
            area = cv2.contourArea(cnt_green)
            approx = cv2.approxPolyDP(cnt_green, 0.02*cv2.arcLength(cnt_green, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if area > 2500:
                cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)

                if len(approx) == 3:
                    cv2.putText(image, "Arriving at Checkpoint", (x, y), font, 1, (0, 0, 0))
                    print("Green Triangle detected!")
                    d = 1
                    
                elif len(approx) == 4:
                    cv2.putText(image, "Go left", (x, y), font, 1, (0, 0, 0))
                    print("Green Rectangle detected!")
                    c = 1

                if c == 1:
                    print("Going left")
                    ser.write(str('3').encode())
                    time.sleep(1)

                if d == 1:
                    print("Stopping program")
                    ser.write(str('0').encode())
                    time.sleep(1)


        cv2.imshow("Image", image)
        cv2.imshow("Mask Red", mask_red)
        cv2.imshow("Mask Green", mask_green)

        key = cv2.waitKey(1)
        rawCapture.truncate(0)
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    camera.stop_recording()


except Exception as e:
    print("[INFO] Error: " + str(e))




