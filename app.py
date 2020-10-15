import pyautogui
import sys
import keyboard
import time
import numpy as np 
import cv2
from matplotlib import pyplot as plt
import imutils

# CURSOR MOVEMENT #
# print(pyautogui.size())
# pyautogui.moveTo(960, 540, duration = 0)


img = cv2.imread("1.jpg")

img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

lower_range = np.array([5, 50, 50], dtype=np.uint8) 
upper_range = np.array([70, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_range, upper_range)

# mask = cv2.erode(mask, None, iterations=2)
# mask = cv2.dilate(mask, None, iterations=2)


	# find contours in the mask and initialize the current
	# (x, y) center of the object
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
#cnts = cnts[0] if imutils.is_cv2() else cnts[1]
center = None




# only proceed if at least one contour was found
if len(cnts) > 0:
	# find the largest contour in the mask, then use
	# it to compute the minimum enclosing circle and
	# centroid
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)

	# print(M["m10"])
	# print(M["m00"])
	# print(M["m01"])
	# print(M["m00"])

	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	# center = (0,0)

	# only proceed if the radius meets a minimum size
	if radius > 1:
		#draw the circle and centroid on the frame,
		#then update the list of tracked points
		cv2.circle(img, (int(x), int(y)), int(radius),(0, 255, 255), 2)
		cv2.circle(img, center, 5, (0, 0, 255), -1)
		print(x)
		print(y)

# cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('image',img)


while(1):
  k = cv2.waitKey(0)
  cv2.destroyAllWindows()
  sys.exit()

# # CATCHING IF KEY WAS PRESSED # 
# message = "WAITING"
# while True:
# 	if keyboard.is_pressed('q'):
# 		message = "PRESSED"
# 	print(message)
# 	time.sleep(1)


#C 180 Z 150 M 118
# Hue 31
# Sat 34.4
# Val 70.6