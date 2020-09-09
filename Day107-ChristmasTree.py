from turtle import *
from random import randint
import time

myPen = Turtle()
myPen.shape("turtle")
myPen.speed(10)

window = Screen()
window.bgcolor("#69D9FF")

y = -100
width = 240


def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_triangle(turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
    turtle.setheading(0)


def draw_square(turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)


def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)


def draw_star(turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(144)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)

def addtext(x, y, text, color, size):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.color(color)
    myPen.write(text, None, align="center", font=("Times", size, "normal"))
    myPen.hideturtle()

# Trunk of the tree
draw_rectangle(myPen, "brown", -15, y-40, 30, 40)

# Tree
while width>20:
  width = width - randint(20,30)
  height = randint(15,35)
  x = 0 - width/2
  draw_rectangle(myPen, "green", x, y, width, height)
  y = y + height

# Star
draw_star(myPen, "yellow", 4, y, 20)

addtext(0, -220, "Merry Christmas!", 'red', "30")

time.sleep(10)
