from picamera.array import PiRGBArray
import picamera
import time
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (1080, 720)
    rawCapture = PiRGBArray(camera)
    time.sleep(10)
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array

    cv2.imshow("image", image)
    cv2.waitKey(0)
