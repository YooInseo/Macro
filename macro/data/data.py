import pyautogui
from pynput.keyboard import Listener, Key, KeyCode

#해당 클래스는 시간과 포지션, 마우스 클릭 여부, 키보드 입력 여부를 담는다.
class data:  
    data = set(); #포지션 값을 담을 리스트
    times = set(); #시간 값을 담을 리스트
    record = False # 레코딩 여부

    
