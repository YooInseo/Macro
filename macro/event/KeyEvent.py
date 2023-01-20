import keyboard
import threading
from pynput import keyboard
from data.data import data
from datetime import datetime
import pyautogui


class KeyEvent:
    isStart = False

    def __init__(self, list):
        self.isStart = True
        self.info = data()
        # self.thread = threading.Thread(target=self.detect) 
        # self.thread.start()

    def detect(self):
        while(True):
            if keyboard.is_pressed("a"):
                print("메크로 시작!")

    def start(self, list):
        while(self.isStart):
            date = datetime.utcnow() 
            point = pyautogui.position()
            list.insertItems()
            print("x: " + str(point[0]) + " y: "+ str(point[1])  + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + ":"+ str(date.microsecond))

    def stop(self):
        self.isStart = False
        print("중지됩니다.")
        # del(self.t)

    def registerKey(self,key):
        print(key," 값으로 변경됨")
        # keyboard.on_press_key(key, lambda _: self.stop())

    def on_press(key):
        try: 
            if(data.startKey is not any):
                print("test" , data.startKey)
                 
        except: 
            print()
                # self.start()
            # print('Alphanumeric key pressed: {0} '.format(
            #     key.char))
        

    def on_release(key):
        # print('Key released: {0}'.format(
        #     key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    
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
