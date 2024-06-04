#Button(window, text="버튼에 표시될 글자", 속성, command=명령어실행및함수호출)
from tkinter import*
window=Tk()
window.title("윈도우 창 연습")
window.geometry("400x500")

button1 = Button(window, text="파이썬 종료", fg="red", command=quit)
button1.pack()
window.mainloop()