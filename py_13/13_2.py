# 형식 Label(윈도우창, text="표시될 글자", 속성값)
# 형식 Label(윈도우창, image="이미지위치및파일명", 속성값)

from tkinter import *
window = Tk()
window.geometry("400x500")
window.resizable(width=False, height=False)

label1 = Label(window, text="SWEDU~~Python을")
label2 = Label(window, text="열심히", font=("궁서체",30), fg="blue")

label3 = Label(window, text="공부 중", bg="magenta", width=20, height=5)

label1.pack() # 배치
label2.pack()
label3.pack()

window.mainloop()