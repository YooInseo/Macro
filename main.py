import sys
from PyQt5       import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

from pynput import keyboard
from PyQt5.QtCore import QThread
from datetime import datetime
import time
from pynput import mouse

import pyautogui

class data:
    startKey = any 
    playing = False
    isRecording = False
    record = set()
    index = 0
    info = dict()

class Macro(QThread):

    def __init__(self, Widget):
        super().__init__() 
        self.entry = Widget.entry
        self.loadButton = Widget.loadButton
        self.newButton = Widget.newButton
        self.startButton = Widget.startButton
        self.settingButton = Widget.settingButton
         
    def run(self):
         
        while(True):
            if(data.isRecording):
                it = QtGui.QStandardItem("마우스 움직임")
                self.entry.appendRow(it)
                
                self.loadButton.setDisabled(True)
                self.newButton.setDisabled(True)
                self.startButton.setDisabled(True)
                self.settingButton.setDisabled(True)
                
                data.record.add(pyautogui.position()) #TODO position 값은 Key로 지정, ClickType은 Value로 지정하여 불러온다.
                # data.info.update({pyautogui.position(): ""})
            
                # if(pyautogui.rightClick()):
                #     print("left click")
                time.sleep(0.1)
            elif data.playing is not True:
                self.loadButton.setDisabled(False)
                self.newButton.setDisabled(False)
                self.startButton.setDisabled(False)
                self.settingButton.setDisabled(False)
                
            else:
                length = len(data.record)
                if (length - 1) != data.index:
                    data.index += 1
                    position = list(data.record)[data.index]
                    pyautogui.moveTo(position[0], position[1])
                    time.sleep(0.1)
                else:
                    data.index=0
                    break
                    
class Listner(QThread):
    def __init__(self):
        super().__init__()  
  
    def on_press(self,key):
        try: 
            #TODO 특수 키를 입력하기 위해선 except를 사용 해야 하는데, 해당 방법을 사용 할 경우, 강제적으로 일반 키보드도 넣어줘야한다.
            #리펙토링 필요함.

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
        

class Widget(QtWidgets.QWidget): #TODO 저장, 초기화 버튼 만들기
 
    def __init__(self):
        super().__init__()
        lay = QtWidgets.QVBoxLayout(self)
 
        self.setWindowTitle("Macro")
        self.setGeometry(1000, 200, 300, 300)

        self.listView = QtWidgets.QListView()
        self.label    = QtWidgets.QLabel("")
        self.recordButton = QtWidgets.QPushButton()

        self.combo_box = QtWidgets.QComboBox()

        self.combo_box.setGeometry(0, 0, 300, 100)
        
        self.combo_box.currentTextChanged.connect(self.changeKey)

        names = [member.name for member in keyboard.Key]
        self.combo_box.addItems(names)

        self.hlay = QtWidgets.QHBoxLayout()

        lay.addLayout(self.hlay)

        self.clearButton = QtWidgets.QPushButton("초기화")
        self.clearButton.setToolTip("모든 메크로 기록을 지웁니다.")  

        self.saveButton = QtWidgets.QPushButton("저장")
        self.saveButton.setToolTip("메크로를 새로 만듭니다.")  

        self.hlay.addWidget(self.clearButton)

        self.newButton = QtWidgets.QPushButton("새로 만들기")
        self.newButton.setToolTip("메크로를 새로 만듭니다.")        

        self.loadButton = QtWidgets.QPushButton("불러오기")
        self.loadButton.setToolTip("저장한 메크로를 불러옵니다.") 
        # self.loadButton.setDisabled(True)       

        self.startButton = QtWidgets.QPushButton("재생")
        self.startButton.clicked.connect(self.playRecord)

        self.settingButton = QtWidgets.QPushButton("설정")
        lay.addWidget(self.combo_box)
        lay.addWidget(self.listView)

        self.hlay = QtWidgets.QHBoxLayout()
        
        lay.addLayout(self.hlay)

        self.hlay.addWidget(self.newButton)
        self.hlay.addWidget(self.loadButton)
        self.hlay.addWidget(self.startButton)
        self.hlay.addWidget(self.settingButton)

        self.entry = QtGui.QStandardItemModel()
        self.listView.setModel(self.entry)

        self.listView.clicked[QtCore.QModelIndex].connect(self.on_clicked)

        self.Thread1 = Listner()
        self.Thread1.start()
        
        self.macro = Macro(self) #TODO 메크로를 병렬 처리 하여, 만약, 
        self.macro.start()

    def playRecord(self):
        data.playing = True
        
    def changeKey(self):
            data.startKey = self.combo_box.currentText()
            print(data.startKey + "해당 키로 단축키가 바뀜")
    

    def on_clicked(self, index):
        item = self.entry.itemFromIndex(index)
        self.label.setText("on_clicked: itemIndex=`{}`, itemText=`{}`"
                           "".format(item.index().row(), item.text()))
        self.itemOld = item

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())