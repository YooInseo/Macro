import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from pynput import keyboard
import time
from datetime import datetime

class data:
    startKey = any 
    isRecording = False
    record = set()
 

  
class Macro(QThread):

    def __init__(self):
        super().__init__()  

    def run(self):
        while(True):
            if(data.isRecording):
                now = datetime.now()
                print(now)
                # data.record.add(time.time)
            time.sleep(0.1)

class Listner(QThread):
    def __init__(self):
        super().__init__()  
  
    def on_press(self,key):
        try:
            if data.startKey is not any: #startKey 값이 any 타입이 아닐 경우 
                if (str(key).replace("Key.","")) == data.startKey: 
                    print(f'알파벳 \'{key.char}\' 눌림ㅎㅎ' )

        except AttributeError:
              if data.startKey is not any:
                #일반 알파벳 키가 아닌 특수 키일 경우, Key.cmd 와 같은 형식으로 key값이 반환 되므로,
                #  해당 문자열을 공백으로 바꾼 후, 데이터에 존재하는 키와 비교한다.
                if str(key).replace("Key.","") == data.startKey: 
                    if data.isRecording is not True:
                        data.isRecording = True
                    else:
                        data.isRecording = False
                     
 
    def on_release(self,key):
        if key == keyboard.Key.esc:
            # esc 키에서 풀림
            return False

    def run(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
         listener.join()
    

class MyWindow(QMainWindow):
         
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Macro")
        self.setGeometry(1000, 200, 300, 300)

        self.UIComponents()
        
        self.Thread1 = Listner()
        self.Thread1.start()
        
        self.macro = Macro() #TODO 메크로를 병렬 처리 하여, 만약, 
        self.macro.start()

         

    def changeKey(self):
        data.startKey = self.combo_box.currentText()
        print(data.startKey + "해당 키로 단축키가 바뀜")
   

    def UIComponents(self):

        self.label = QLabel("My text")
        self.label.setGeometry(100,0,300,100)

        self.combo_box = QComboBox(self)
  
        self.combo_box.setGeometry(0, 0, 300, 100)
        
        self.combo_box.currentTextChanged.connect(self.changeKey)

        names = [member.name for member in keyboard.Key]
        self.combo_box.addItems(names)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()

    app.exec_()