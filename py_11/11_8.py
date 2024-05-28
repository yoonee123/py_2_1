import turtle as t

def draw(x, y):
    t.goto(x, y)
    
t.shape("turtle")
t.pensize(5)
s = t.Screen()
s.onscreenclick(draw)
input()