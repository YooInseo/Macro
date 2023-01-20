import threading
from datetime import datetime
import time
import pyautogui
import datetime as dt
from data import data
from event.KeyEvent import KeyEvent
from pynput.keyboard import Listener, Key

class Macro:
    def __init__(self, info):
        self.info = info

    def startRecord(list):    
        # print("Current date:",datetime.utcnow())
        # date = datetime.utcnow() 
        KeyEvent(list)
        # print(str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + ":"+ str(date.microsecond))

        # seconds =(date.total_seconds())
        # milliseconds = round(seconds*1000)
        # print("Milliseconds since epoch:",milliseconds)
        # data.record = True

        # # while(data.record):
        # #     # print("기록이 시작 됩니다." + str(pyautogui.position.x))

        # #     time.sleep(1)
        # self.data.record = True # 레코딩 시작


    def stopRecord(self):
        print("기록이 중지 됩니다.")


    def playRecord(self):
        print("기록을 재생합니다.")
    
    def getTime():
        date = datetime.utcnow()  
 
        seconds =(date.total_seconds())
        milliseconds = round(seconds*1000)

    def getInfo(self):
        return self.info