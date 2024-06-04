from tkinter import*
import tkinter.messagebox
#함수 정의 부분
def myFunc() :
    tkinter.messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠?")
    
def myFunc2() :
    tkinter.messagebox.showinfo("버튼","버튼 수업중")
#main
window = Tk()
window.title("윈도우 창 연습")
window.geometry("400x500")

photo = PhotoImage(file="gif/dog2.gif")
button1 = Button(window, image=photo, command=myFunc)
button2 = Button(window, text="버튼2", command=myFunc2)
button1.pack()
button2.pack()

window.mainloop()