import turtle
import time

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(500)
pen.hideturtle()

window = turtle.Screen()
window.title('Thank You, Frontliners!')

def drawCircle(x, y, color, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()


def drawStar(x, y, color, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(5):
        pen.right(144)
        pen.forward(size)
    pen.end_fill()


def addText(x, y, text, color, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.write(text, None, align="center", font=("Arial", size, "normal"))

red = "#FF0000"
orange = "#FFA600"
yellow = "#FFFF00"
green = "#62FF00"
blue = "#1E56FC"
indigo = "#4800FF"
violet = "#CC00FF"
white = "#FFFFFF"
skyblue = "#69C5FF"

window.bgcolor(skyblue)

drawCircle(0,-360,red,180)
drawCircle(0,-360,orange,170)
drawCircle(0,-360,yellow,160)
drawCircle(0,-360,green,150)

drawCircle(0,-360,blue,140)
drawCircle(0,-360,indigo,130)
drawCircle(0,-360,violet,120)
drawCircle(0,-360,skyblue,110)

drawStar(-100,130,blue,40)
drawStar(145,130,yellow,40)

addText(0,150,"Thank you for",white,"28")
addText(0,120,"your service",red,"28")
addText(0,90,"frontliners!",white,"28")

time.sleep(30)
