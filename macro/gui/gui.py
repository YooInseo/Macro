import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QComboBox, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from data.macro import Macro 
from data.data import data
from event.KeyEvent import KeyEvent

class window():
   def __init__(self):

      app = QApplication(sys.argv)
      widget = QWidget()

      info = data()
      macro = Macro(info)

      keyList = data.keyList
      
      self.cb = QComboBox(widget)  
      # self.cb.currentTextChanged.connect(self.registerKey)

      for a in keyList: #키값 리스트를 콤보박스에 추가
         self.cb.addItem(a)

      self.cb.move(55, 0)
      # cb.itemsel.connect(lambda: print("test"))
      list = QListWidget(widget)
      list.move(0, 30)
       # cb = QComboBox("TEST", widget)
      # cb.addItem("C")
      # cb.addItem("C++")
      # cb.addItems(["Java", "C#", "Python"])
      # self.cb.currentIndexChanged.connect(self.selectionchange)
 
      btnRecord = QPushButton("기록",widget)	# 버튼 텍스트
      # btnRun.move(20, 20)	# 버튼 위치
 
      btnRecord.clicked.connect(lambda: macro.startRecord(list))	# 버튼 클릭 시 이벤트 연결

      widget.setGeometry(1000,450,320,200)
      widget.setWindowTitle("Macro Recorder")
      widget.show()


      sys.exit(app.exec_())
  

   #Change key of the start 
   # def registerKey(self, value):
      # listner = KeyEvent(self.cb)
      # listner.registerKey(value)
 

 