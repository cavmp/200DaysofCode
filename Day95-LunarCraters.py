import turtle
import time
from random import randint

myPen = turtle.Turtle()
myPen.speed(0)
screen = turtle.Screen()
screen.bgcolor("#111155")
myPen.color("#888888")
myPen.pensize(3)
myPen.penup()
myPen.goto(0, 0)


def drawMoon(x, y, radius):
    myPen.penup()
    myPen.goto(x, y - radius)
    myPen.pendown()
    myPen.fillcolor("#AAAAAA")
    myPen.begin_fill()
    myPen.circle(radius)
    myPen.end_fill()


def drawCrater(x, y, radius):
    myPen.pensize(1)
    myPen.penup()
    myPen.goto(x, y - radius)
    myPen.pendown()
    myPen.fillcolor("#AAAAAA")
    myPen.begin_fill()
    myPen.circle(radius)
    myPen.end_fill()


# Draw the Moon
MOON_RADIUS = 160
drawMoon(0, 0, MOON_RADIUS)
# Add 20 craters on the Moon's surface
for i in range(20):
    radius = randint(3, 50)
    distance = MOON_RADIUS
    while (distance + radius > MOON_RADIUS):
        x = randint(-MOON_RADIUS, MOON_RADIUS)
        y = randint(-MOON_RADIUS, MOON_RADIUS)
        # Apply Pythagoras Theorem to calulate the distance from the centre
        distance = (x ** 2 + y ** 2) ** 0.5
    drawCrater(x, y, radius)

myPen.hideturtle()
myPen.getscreen().update()
time.sleep(5)
