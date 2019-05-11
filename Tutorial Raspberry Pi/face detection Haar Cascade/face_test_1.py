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

font = cv2.FONT_HERSHEY_COMPLEX
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.rotation = 180

rawCapture = PiRGBArray(camera, size=(640, 480))

try:
    ser = serial.Serial('/dev/ttyACM1', 9600)
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        a = 0

        
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

            if a == 0:
                print("Initiating program")
                ser.write(str('0').encode())
                time.sleep(1)


        cv2.imshow("Image", image)
        key = cv2.waitKey(1)
        rawCapture.truncate(0)
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
 

except Exception as e:
    print("[INFO] Error: " + str(e))




