import keyboard
import threading
from datetime import datetime
import pyautogui

class KeyEvent:
    isStart = False
    def __init__(self):
        self.isStart = True
        t = threading.Thread(target=self.start)
        t.start()
        keyboard.on_press_key("r", lambda _: self.stop())
        
    def start(self):
        while(self.isStart):
            date = datetime.utcnow() 
            point = pyautogui.position()
 
            print("x: " + str(point[0]) + " y: "+ str(point[1])  + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + ":"+ str(date.microsecond))

    def stop(self):
        self.isStart = False
        print("중지됩니다.")
# while True:
#     if keyboard.read_key() == "p":rrrrrrrrrrrrrrrrrrrr
#         print("You pressed p")
#         break


 
