from tkinter import*
mycolor = "blue"
def paint(event):
    x1, y1 = ( event.x ), ( event.y )
    x2, y2 = ( event.x ), ( event.y )
    canvas.create_oval( x1, y1, x2, y2, fill = mycolor)   
    
def change_color():
    global mycolor
    mycolor = "red"
    
window = Tk()
canvas = Canvas(window) 
canvas.pack()
canvas.bind("<B1-Motion>", paint)

button = Button(window, text="빨강색", command=change_color)
button.pack(side=RIGHT, padx=10)
window.mainloop()

    