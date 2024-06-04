from tkinter import*
import tkinter.messagebox

window = Tk()
window.title("윈도창 연습")
window.geometry("400x100")
#함수 정의 부분
def myFunc() :
    if chk.get() == 0 :
        tkinter.messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        tkinter.messagebox.showinfo("", "체크버튼이 켜졌어요.")
#main
chk = IntVar()
cb1 = Checkbutton(window, text="클릭1", variable=chk, command=myFunc)
cb1.pack()

window.mainloop()