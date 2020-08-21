import turtle
import random
import time

myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(500)

window = turtle.Screen()
window.bgcolor("#69C5FF")

skinColors = ["#FCD09D", "#FAC47A", "#DBA965", "#CC9D5E", "#A3855B", "#806645", "#665135"]
eyeColors = ["#489CF0", "#15A315", "#8C3303"]
hairColors = ["#000000", "#8C3303", "#F5D907", "#580000", "#E31E00", "#636363", "#FFFFFF"]

myPen.hideturtle()
myPen.penup()
myPen.goto(0, -100)

skincolor=int(input("Chose a skin complexion from 1 (pale) to 7 (dark skin)? "))-1
eyecolor=int(input("Color of the eyes? Chose between 1 - blue, 2 - green, 3 - brown. "))-1
haircolor=int(input("Hair color? Chose between 1 - black, 2 - brown, 3 - Blond, 4 - Auburn, 5 - Red, 6 - Grey, 7 - White. " ))-1

def drawHair():
    # Drawing the hair
    myPen.penup()
    myPen.goto(-50, -50)
    myPen.pendown()
    myPen.color(hairColors[haircolor])
    myPen.fillcolor(hairColors[haircolor])
    myPen.begin_fill()
    myPen.goto(-160, 20 + random.randint(-10, 10))
    myPen.goto(-140, 110 + random.randint(-10, 10))
    myPen.goto(-130, 100 + random.randint(-10, 10))
    myPen.goto(-110, 160 + random.randint(-10, 10))
    myPen.goto(-90, 150 + random.randint(-10, 10))
    myPen.goto(-70, 180 + random.randint(-10, 10))
    myPen.goto(-50, 160 + random.randint(-10, 10))
    myPen.goto(-40, 190 + random.randint(-10, 10))
    myPen.goto(-10, 160 + random.randint(-10, 10))
    myPen.goto(20, 180 + random.randint(-10, 10))
    myPen.goto(50, 160 + random.randint(-10, 10))
    myPen.goto(70, 150 + random.randint(-10, 10))
    myPen.goto(90, 160 + random.randint(-10, 10))
    myPen.goto(110, 140 + random.randint(-10, 10))
    myPen.goto(130, 170 + random.randint(-10, 10))
    myPen.goto(140, 110 + random.randint(-10, 10))
    myPen.goto(160, 20 + random.randint(-10, 10))
    myPen.goto(-50, -50)
    myPen.end_fill()


def drawFace():
    # Drawing the face
    myPen.penup()
    myPen.goto(0, -150)
    myPen.color(skinColors[skincolor])
    myPen.fillcolor(skinColors[skincolor])
    myPen.begin_fill()
    myPen.circle(150)
    myPen.end_fill()


def drawSmile():
    # Drawing the smile
    myPen.penup()
    myPen.goto(0, -100)
    myPen.color("#F00070")
    myPen.fillcolor("#F00070")
    myPen.begin_fill()
    myPen.circle(70)
    myPen.end_fill()

    myPen.penup()
    myPen.goto(0, -85)
    myPen.color(skinColors[skincolor])
    myPen.fillcolor(skinColors[skincolor])
    myPen.begin_fill()
    myPen.circle(80)
    myPen.end_fill()


def drawEyeBrow(x):
    # Drawing one eyeBrow at position x
    myPen.penup()
    myPen.goto(x, 50)
    myPen.color(hairColors[haircolor])
    myPen.fillcolor(hairColors[haircolor])
    myPen.begin_fill()
    myPen.circle(30)
    myPen.end_fill()

    myPen.penup()
    myPen.goto(x, 20)
    myPen.color(skinColors[skincolor])
    myPen.fillcolor(skinColors[skincolor])
    myPen.begin_fill()
    myPen.circle(40)
    myPen.end_fill()


def drawEye(x):
    # Drawing one eyeBrow at position x
    myPen.penup()
    myPen.goto(x, 20)
    myPen.color("#000000")
    myPen.fillcolor("#FFFFFF")
    myPen.begin_fill()
    myPen.circle(30)
    myPen.end_fill()

    myPen.penup()
    myPen.goto(x, 30)
    myPen.color(eyeColors[eyecolor])
    myPen.fillcolor(eyeColors[eyecolor])
    myPen.begin_fill()
    myPen.circle(20)
    myPen.end_fill()

    myPen.penup()
    myPen.goto(x, 40)
    myPen.color("#000000")
    myPen.fillcolor("#000000")
    myPen.begin_fill()
    myPen.circle(10)
    myPen.end_fill()


drawHair()
drawFace()
drawSmile()
drawEyeBrow(-60)
drawEyeBrow(60)
drawEye(-60)
drawEye(60)

myPen.penup()
myPen.goto(200, 240)

time.sleep(20)
