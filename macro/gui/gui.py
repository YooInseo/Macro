import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from data.macro import Macro
import pyautogui

class window():

   def __init__(self):
      app = QApplication(sys.argv)
      widget = QWidget()
      macro = Macro()
      

      cb = QComboBox(widget)
      cb.addItem('Option1')
      cb.addItem('Option2') 0                                     
      cb.addItem('Option3')
      cb.addItem('Option4')
      cb.move(100, 0)
      # cb = QComboBox("TEST", widget)
      # cb.addItem("C")
      # cb.addItem("C++")
      # cb.addItems(["Java", "C#", "Python"])
      # self.cb.currentIndexChanged.connect(self.selectionchange)
      # cb.move(50, 50)
      btnRecord = QPushButton("기록",widget)	# 버튼 텍스트
      # btnRun.move(20, 20)	# 버튼 위치
   
      btnRecord.clicked.connect(lambda: Macro.startRecord(macro))	# 버튼 클릭 시 이벤트 연결

   

      # btnStart = QPushButton("재생",widget)	# 버튼 텍스트
      # btnStart.move(0, 20)	# 버튼 위치
      # btnStart.clicked.connect(lambda: Macro.playRecord(macro))	# 버튼 클릭 시 이벤트 연결

      # btnStop = QPushButton("Stop",widget)	# 버튼 텍스트
      # btnStop.move(0, 40)	# 버튼 위치
      # btnStop.clicked.connect(lambda: Macro.stopRecord)	# 버튼 클릭 시 이벤트 연결

      # textLabel = QLabel(widget)
      # textLabel.setText("Hello World!")
      # textLabel.move(110,85)
   
      widget.setGeometry(1000,450,320,200)
      widget.setWindowTitle("Macro Recorder")
      widget.show()
      sys.exit(app.exec_())

 