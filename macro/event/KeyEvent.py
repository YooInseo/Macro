import keyboard
import threading
from datetime import datetime
import pyautogui

class KeyEvent:
    isStart = False
    def __init__(list, self):
        self.isStart = True
        t = threading.Thread(target=self.start,args=(list))
        t.start()
        keyboard.on_press_key("r", lambda _: self.stop())
        
    def start(list, self):
        while(self.isStart):
            date = datetime.utcnow() 
            point = pyautogui.position()
            list.insertItems()
            print("x: " + str(point[0]) + " y: "+ str(point[1])  + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + ":"+ str(date.microsecond))

    def stop(self):
        self.isStart = False
        print("중지됩니다.")
# while True:
#     if keyboard.read_key() == "p":rrrrrrrrrrrrrrrrrrrr
#         print("You pressed p")
#         break


 

# from pynput.keyboard import Listener, Key
 
# store = set()

# oldx = oldy = -1

# def on_mouse(event, x, y, flags, param):
#    global oldx, oldy
#    cv2.EVENT_
# #    if event == cv2.EVENT_LBUTTONDOWN:
# #        oldx, oldy = x, y
# #    else event == cv2.EVENT_MOUSEMOVE:
# #        if flags & cv2.EVENT_FLAG_LBUTTON:
# #            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
# #            cv2.imshow('image', img)
# #            oldx, oldy = x, y


# # pyautogui.typewrite(['a', 'b', 'c'], interval=0.1)


# def handleKeyPress( key ):
#     store.add( key )
 
#     print( 'Press: {}'.format( store ) )
 
# def handleKeyRelease( key ):
#     print( 'Released: {}'.format( key ) )
 
#     if key in store:
#         store.remove( key )
        
#     # 종료
#     if key == Key:
#         return False
 
 
# with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
#     listener.join()
