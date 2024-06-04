#pack(side=LEFT/TOP/RiGHT/BOTTOM,padx=여백지정,pady=여백지정) 배치
from tkinter import*
window = Tk()
button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")
# button1.pack(side=LEFT, padx=15)
# button2.pack(side=LEFT, padx=15)
# button3.pack(side=LEFT, padx=15)

# button1.pack(side=TOP, padx=15 ,pady=15)
# button2.pack(side=TOP, padx=15)
# button3.pack(side=TOP, padx=15)

# button1.pack(side=BOTTOM, padx=15 ,pady=15)
# button2.pack(side=BOTTOM, padx=15)
# button3.pack(side=BOTTOM, padx=15)

button1.pack(side=RIGHT, padx=15 ,pady=15)
button2.pack(side=RIGHT, padx=15)
button3.pack(side=RIGHT, padx=15)

window.mainloop()