#위젯.Bind("이벤트", 함수)

from tkinter import *
import tkinter.messagebox

#함수 정의 부분
def clickLeft(event) :
    tkinter.messagebox.showinfo("마우스", "왼쪽 마우스가 클릭됨")

#main
window = Tk()

window.bind("<Button-1>", clickLeft)    #이벤트처리, 왼쪽마우스버튼클릭 이벤트
#<Button-3>으로 바꾸면 오른쪽마우스클릭
window.mainloop()
