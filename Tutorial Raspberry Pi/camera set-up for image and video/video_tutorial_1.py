import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.rotation = 180
    camera.start_preview()
    camera.start_recording('/home/pi/marker3.h264')
    time.sleep(60)
    camera.stop_recording()
    camera.stop_preview()

