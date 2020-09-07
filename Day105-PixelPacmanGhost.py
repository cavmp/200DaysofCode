import turtle
import time

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")


# Draws a box and fills using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)


boxSize = 15

myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)

# Using a "list of lists" = pixel art is stored
palette = ["#FFFFFF", "#FF0000", "#0000ff"]
pixels = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]

pixels.append([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0])
pixels.append([0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0])
pixels.append([0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0])
pixels.append([0, 1, 1, 0, 0, 2, 2, 1, 1, 0, 0, 2, 2, 0])
pixels.append([1, 1, 1, 0, 0, 2, 2, 1, 1, 0, 0, 2, 2, 1])
pixels.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1])
pixels.append([1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1])

for i in range(0, len(pixels)):
    for j in range(0, len(pixels[i])):
        myPen.color(palette[pixels[i][j]])
        box(boxSize)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.pendown()
    myPen.setheading(270)
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180)
    myPen.forward(boxSize * len(pixels[i]))
    myPen.setheading(0)
    myPen.pendown()

myPen.getscreen().update()

time.sleep(15) # Pauses program for 15 seconds
