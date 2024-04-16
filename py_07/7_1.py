import turtle

colors = ["red", "blue", "purple", "green", "yellow", "orange"]
t = turtle.Turtle()
turtle.bgcolor("black")

t.width(3)
length = 10
while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6]) #길이를 6으로 나눠 나머지 수로 색깔을 계속 변환
    t.right(89)
    length = length + 5