
"""Copyright [2017] [Siddhant Mahapatra]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://github.com/Robosid/SLAMBOT/blob/master/License.pdf
    https://github.com/Robosid/SLAMBOT/blob/master/License.rtf

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""



from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import os
from fractions import Fraction
import cv2 #opencv

#setup the camera

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
camera.sensor_mode = 3
camera.rotation = 90
#camera.exposure_compensation = 0
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
#camera.awb_mode = 'off'
#camera.awb_gains = g
#camera.contrast = 10
camera.brightness = 50
camera.saturation = 50 #brighter colours
camera.ISO = 100
rawCapture = PiRGBArray(camera, size=(640,480))

img_counter = 0
dirname = 'calibration'

time.sleep(0.1) #wait for the camera to warm up

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

	image = frame.array
	#hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	cv2.imshow("Camera Frame",image)

	k = cv2.waitKey(1)
	
	if k%256 == 27:
		#ESC PRESSED
		print("------------------------------")
		print("Escape hit, closing .....")
		print("------------------------------")
		print("\n")
		break
	elif k%256 == 32:
		#SPACE PRESSED
		img_name = "opencv_image_{}.png".format(img_counter)
		cv2.imwrite(os.path.join(dirname, img_name), image)
		print("------------------------------")
		print("{} saved!".format(img_name))
		print("------------------------------")
		print("\n")
		img_counter += 1
	rawCapture.truncate(0) #clear steam for next frame
