import turtle #터틀 그래픽 모듈을 불러옴
import random #랜덤 모듈을 불러옴 

screen = turtle.Screen()
image1 = "front.gif"
image2 = "back.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
coin = random.randint(0, 1)
if coin == 0 :
    t1.shape(image1)
else :
    t1.shape(image2)
