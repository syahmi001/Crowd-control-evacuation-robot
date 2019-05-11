import numpy as np
import cv2
import time
import imutils
from picamera.array import PiRGBArray
from picamera import PiCamera

marker_path = "/home/pi/Downloads/x.jpg"
marker_intruder = cv2.resize(cv2.imread(marker_path), (0, 0), fx=0.5, fy=0.5)
marker_intruder = cv2.cvtColor(marker_intruder, cv2.COLOR_BGR2GRAY)
threshold = .7
storedMarkers = {}
scales = [0.4, 0.7, 1]

def storingMarkerScale(marker):
    for scale in scales:
        resized = imutils.resize(marker, width=int(marker.shape[1]*scale))
        storedMarkers[str(scale)] = resized

# This method takes in consideration 3 resized images for the marker
# It will apply template matching for the scale you consider helpful
# Remember that it will run template matching so it will be heavy for the camera frames
def multiScaleTemplateMatching(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    found = []
    w = 0
    h = 0
    for scale in scales:
        marker = storedMarkers[str(scale)]
        w, h = marker.shape[::-1]
        res = cv2.matchTemplate(image_gray, marker, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        if zip(*loc[::-1]):
            found = zip(*loc[::-1])
            break
    for pt in found:
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)


# initializing the camera
def startCamera():
    print("Warming up camera")
    resolution = (640, 480)

    camera = PiCamera()
    camera.resolution = resolution
    camera.framerate = 16

    rawCapture = PiRGBArray(camera, size=resolution)

    time.sleep(0.1)
    print ("Starting to patrol")
    for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame = f.array
        multiScaleTemplateMatching(frame)
        cv2.imshow("Security", frame)
        key = cv2.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        if key == ord("q"):
            break


# First we will scale the marker once so we don't resize them each time
storingMarkerScale(marker_intruder)
startCamera()
