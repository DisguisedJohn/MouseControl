import sys
import numpy as np
import cv2
blue = 118
green = 150
red = 180  
color = np.uint8([[[blue, green, red]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
hue = hsv_color[0][0][0]
print("Lower bound is :"),
print("[" + str(hue-10) + ", 100, 100]\n")
print("Upper bound is :"),
print("[" + str(hue + 10) + ", 255, 255]")