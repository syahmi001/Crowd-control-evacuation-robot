from picamera.array import PiRGBArray
import picamera
import time
import cv2
import argparse

face_cascade = cv2.CascadeClassifier("/home/pi/Camera_test/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('/home/pi/Camera_test/haarcascade_eye.xml')


with picamera.PiCamera() as camera:
    camera.resolution = (1088, 720)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(1088, 720))
    
    time.sleep(0.1)
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]

            
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


        cv2.imshow("Frame", image)
        key=cv2.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        if key == ord("q"):
            break
