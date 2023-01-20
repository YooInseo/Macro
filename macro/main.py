import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from pynput import keyboard
from data.data import data
 

class MyThread(QThread):
    cnt=0
    running= False

    def __init__(self):
        super().__init__()  
  
    def on_press(self,key):
        try:
            if data.startKey is not any:
                print(key.char)
                print(str(key.char == data.startKey))
                if key == data.startKey:
                    print(f'알파벳 \'{key.char}\' 눌림ㅎㅎ' )
                    
        except AttributeError:
              if data.startKey is not any:
                if str(key).replace("Key.","") == data.startKey:
                    print("test")
                    # print(f'특수키 \'{key.char}\' 눌림ㅎㅎ' ) 
 
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

        self.Thread1 = MyThread()
        self.Thread1.start()
        self.UIComponents()

    def changeKey(self):
        data.startKey = self.combo_box.currentText()
        print(data.startKey + "해당 키로 단축키가 바뀜")
   

    def UIComponents(self):

        self.label = QLabel("My text")
        self.label.setGeometry(100,0,300,100)
        # self.layout.addWidget(self.label)

        self.combo_box = QComboBox(self)
  
        # setting geometry of combo box
        self.combo_box.setGeometry(0, 0, 300, 100)
        
        
        #TODO 바뀐 값을 키에 등록 해야함.
        self.combo_box.currentTextChanged.connect(self.changeKey)
        # values = [e.value for e in Color]

        names = [member.name for member in keyboard.Key]
        print(names) 
        # print(keyboard.Key.list)
        self.combo_box.addItems(names)

        # adding items to combo box
        # adding Geek to the combobox
        # combo_box.addItem("Geek")
        # adding Super Geek to the combobox
        # combo_box.addItem("Super Geek")
        # adding Ultra Geek to the combobox
        # combo_box.addItem("Ultra Geek")
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()

    app.exec_()