import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    for i in range(5):
        time.sleep(5)
        camera.capture('/home/pi/image%s.jpg' % i)
    camera.stop_preview()

#image go out 0-4# 
