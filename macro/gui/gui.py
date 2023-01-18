import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QComboBox, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from data.macro import Macro
import pyautogui
 
class window():

   def __init__(self):
      app = QApplication(sys.argv)
      widget = QWidget()
      macro = Macro()
      
      #키값 리스트 생성
      keyList = ['T', 'n', 'r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']
      
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
   
      btnRecord.clicked.connect(lambda: Macro.startRecord(list, macro))	# 버튼 클릭 시 이벤트 연결

      widget.setGeometry(1000,450,320,200)
      widget.setWindowTitle("Macro Recorder")
      widget.show()


      sys.exit(app.exec_())

   def key():
      print("key")

 