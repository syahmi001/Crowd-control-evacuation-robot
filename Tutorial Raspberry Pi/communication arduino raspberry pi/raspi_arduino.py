from picamera.array import PiRGBArray
import serial
import picamera
import time
import cv2
import argparse

face_cascade = cv2.CascadeClassifier("/home/pi/Camera_test/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('/home/pi/Camera_test/haarcascade_eye.xml')

try:
    ser = serial.Serial('/dev/ttyACM1', 9600)
    
    with picamera.PiCamera() as camera:
        camera.resolution = (1088, 720)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(1088, 720))
    
        time.sleep(0.1)
    
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            a = 0
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            time.sleep(1) 
            

            for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = image[y:y+h, x:x+w]
                print("Pro player")
                a = 1
                
            if a == 1:
                print("Pro player")
                ser.write(str('1').encode())

            else:
                print("Noob reported")
                ser.write(str('0').encode())

            cv2.imshow("Frame", image)
            key=cv2.waitKey(1) & 0xFF

            rawCapture.truncate(0)

            if key == ord("q"):
                break

except Exception as e:
    print("[INFO] Error: " + str(e))



