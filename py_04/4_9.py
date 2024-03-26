import turtle #터틀 그래픽 모듈을 불러온다

t = turtle.Turtle()
t.shape("turtle")

t.penup() # 펜을 올려서 그림이 그려지지 않게 함
t.goto(100, 100)
t.write("양수 위치")
t.goto(100, 0)
t.write("0 위치")
t.goto(100, -100)
t.write("음수 위치")

t.goto(0,0)
t.pendown() # 펜을 내려서 그림이 그려지게 함 
s=turtle.textinput("", "숫자을 입력하세요 : ")
n=int(s)
if(n > 0):
    t.goto(100, 100)
elif(n == 0):
    t.goto(100, 0)
else:
    t.goto(100, -100)
