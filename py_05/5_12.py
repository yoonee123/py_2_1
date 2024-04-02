import turtle
t=turtle.Turtle()
t.shape("turtle")

s=turtle.textinput("", "숫자(각형)을 입력하세요 : ")
n=int(s)

for i in range(n):
    t.forward(100)
    t.left(360/n)
s
