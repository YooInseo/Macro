import threading

import time
import pyautogui
import datetime as dt
from data import data

from pynput.keyboard import Listener, Key

class Macro:
    def startRecord(self):
        data.record = True;

        while(data.record):
            print("기록이 시작 됩니다." + str(pyautogui.position.x))

            time.sleep(1)
        self.data.record = True # 레코딩 시작


    def stopRecord(self):
        print("기록이 중지 됩니다.")


    def playRecord(self):
        print("기록을 재생합니다.")

        # self.thread = threading.Thread( target=self.start)
        # self.thread.start() # 스레드 시작




    # data = list(); #포지션 값을 담을 리스트 
    # start = False
    # nowPosition = 0
    # def __init__(self):
    #     self.thread = threading.Thread( target=self.start)
    #     self.thread.start() # 스레드 시작
    
    # def startRecord(self, start):
    #     if(self.nowPosition == 0):
    #         self.nowPosition = pyautogui.position()
    #     while(start):
    #         if(self.nowPosition != pyautogui.position()): # 기존의 값과 다르면 
    #             self.data.append(pyautogui.position())
    #             self.nowPosition = pyautogui.position()
    #             print(self.data)
    #             time.sleep(0.5)
 

    # def stop(self):
    #     self.start = False
    #     self.thread.stop()

    # def record(self):
    #     self.start = True 
