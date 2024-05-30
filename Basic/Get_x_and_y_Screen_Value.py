#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to get the current x and y coordinates of the mouse pointer
================================================================================'''

import pyautogui

while True:
    x, y = pyautogui.position() 
    print(f"Mouse position - X: {x}, Y: {y}")