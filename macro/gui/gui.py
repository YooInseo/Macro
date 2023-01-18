import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QComboBox, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from data.macro import Macro
import pyautogui
 
from data.data import data

class window():
   def __init__(self):
      app = QApplication(sys.argv)
      widget = QWidget()

      info = data()

      macro = Macro(info)

      keyList = data.keyList

      cb = QComboBox(widget)  

      for a in keyList: #키값 리스트를 콤보박스에 추가
         cb.addItem(a)

      cb.move(100, 0)


      list = QListWidget(widget)
      list.move(0, 50)
   
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
 
   def key():
      print("key")

 