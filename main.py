import sys
from PyQt5       import QtWidgets, QtGui, QtCore
from pynput import keyboard
from PyQt5.QtCore import QThread
from datetime import datetime
import time

class data:
    startKey = any 
    isRecording = False
    record = set()

class Macro(QThread):

    def __init__(self, Widget):
        super().__init__() 
        self.entry = Widget.entry
       
         
    def run(self):
        while(True):
            if(data.isRecording):
                now = datetime.now()
                it = QtGui.QStandardItem(str(now))
                self.entry.appendRow(it)
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

class Widget(QtWidgets.QWidget):
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

        self.newButton = QtWidgets.QPushButton("새로 만들기")
        self.loadButton = QtWidgets.QPushButton("불러오기")
        
        lay.addWidget(self.combo_box)
        lay.addWidget(self.listView)

        self.hlay = QtWidgets.QHBoxLayout()
        lay.addLayout(self.hlay)
        self.hlay.addWidget(self.newButton)
        self.hlay.addWidget(self.loadButton)

        self.entry = QtGui.QStandardItemModel()
        self.listView.setModel(self.entry)

        self.listView.clicked[QtCore.QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex() 
        # on the given model index to get a pointer to the item        
        
        # for a in range(100):
        #     it = QtGui.QStandardItem(str(a))
        #     self.entry.appendRow(it)

        self.itemOld = QtGui.QStandardItem("text")

        self.Thread1 = Listner()
        self.Thread1.start()
        
        self.macro = Macro(self) #TODO 메크로를 병렬 처리 하여, 만약, 
        self.macro.start()

    def changeKey(self):
            data.startKey = self.combo_box.currentText()
            print(data.startKey + "해당 키로 단축키가 바뀜")
    

    def on_clicked(self, index):
        item = self.entry.itemFromIndex(index)
        self.label.setText("on_clicked: itemIndex=`{}`, itemText=`{}`"
                           "".format(item.index().row(), item.text()))
        self.itemOld = item

print(__name__)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())