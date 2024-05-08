#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python Script to Convert Text to Speak

--    Note      :   To run this script, you should run it as a root
================================================================================'''

import keyboard
from gtts import gTTS
import vlc

def on_triggered():
   MyObj = gTTS(text='GoodMorning Mr Ahmed' , lang='en' , slow=False)
   #Saving the Converted audio in mp3 file named
   MyObj.save("Welcome.mp3")
   #Play the Converted File
   p = vlc.MediaPlayer("./Welcome.mp3")
   p.play()
   while True:
      pass
   
def listen_for_shortcut():
   # Set the desired shortcut key combination (Ex : Ctrl + Alt + S)
   shortcut = "a + s + d"
   
   # Register the Callback function for the shortcut
   keyboard.add_hotkey(shortcut , on_triggered)
   
   # continuously listen for keyboard events
   keyboard.wait()
   

# Start Listening for the shortcut
listen_for_shortcut()