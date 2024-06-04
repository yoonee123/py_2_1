#이미지 삽입
#PhotoImage(file=이미지경로및 파일명)
#Label(window, image=photo) 이미지 표시

from tkinter import*
window = Tk()
window.title("윈도우 창 연습")
window.geometry("400x500")

photo = PhotoImage(file="gif/dog2.gif")
label1 = Label(window, image=photo)

label1.pack()
window.mainloop()