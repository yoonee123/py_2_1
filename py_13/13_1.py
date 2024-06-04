#tkinter는 파이썬에서 GUI관련 모듈을 제공해주는
#표준 윈도우 라이브러리, 윈도우/리눅스/맥 동일한 코드 사용
#Tk() 베이스 윈도우, 기본이 되는 윈도우 반환

from tkinter import * ##그래픽 환경을 제공하는 모듈 import

window = Tk() #윈도우 창 생성
window.title("윈도우 창 연습") #윈도우 창 제목 생성
window.geometry("400x500") #윈도우 창의 너비, 높이
window.resizable(width=True, height=False) #윈도우 창의 크기조절 유무
#화면을 구성하고 처리하는 부분
window.mainloop() #윈도우 창을 닫지 않고 대기