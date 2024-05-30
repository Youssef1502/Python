#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to open terminal by using string or image compare.
================================================================================'''

import pyautogui
import os
import time


#-------------------------------------------#
#      Open terminal by string only 
#-------------------------------------------#


# pyautogui.hotkey('win')
# time.sleep(1)
# pyautogui.write('terminal')
# pyautogui.hotkey('enter')



#-------------------------------------------#
#      Open terminal by image compare
#-------------------------------------------#

pyautogui.hotkey('win')
time.sleep(1)
pyautogui.write('terminal')

mypath = os.path.dirname(os.path.realpath(__file__))+"/terminal.png"

time.sleep(1)

isfind = None
while isfind is None:
    isfind = pyautogui.locateOnScreen(mypath)
    
print("i got the image")
pyautogui.hotkey('enter')