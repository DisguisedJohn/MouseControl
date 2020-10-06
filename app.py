import pyautogui
import keyboard
import time

# CURSOR MOVEMENT #
# print(pyautogui.size())
# pyautogui.moveTo(960, 540, duration = 0)

# CATCHING IF KEY WAS PRESSED # 
message = "WAITING"
while True:
	if keyboard.is_pressed('q'):
		message = "PRESSED"
	print(message)
	time.sleep(1)
