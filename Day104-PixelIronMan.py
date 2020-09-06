import turtle, time

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")

# This function draws a box
def box(intDim):
    myPen.begin_fill()
    # 0 degrees
    myPen.forward(intDim)
    myPen.left(90)
    # 90 degrees
    myPen.forward(intDim)
    myPen.left(90)
    # 180 degrees
    myPen.forward(intDim)
    myPen.left(90)
    # 270 degrees
    myPen.forward(intDim)
    myPen.end_fill() # Fills the function
    myPen.setheading(0)


boxSize = 10
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)

# A PixelArt is stored using a "list of lists"
colourPalette = ["#FFFFFF", "#000000", "#C90404", "#D4B322", "#7DF0FF"]
pixels = [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]
pixels.append([0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0])
pixels.append([1, 2, 3, 3, 2, 2, 2, 3, 3, 2, 2, 1])
pixels.append([1, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2, 1])
pixels.append([1, 3, 1, 1, 3, 3, 3, 1, 1, 3, 2, 1])
pixels.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1])
pixels.append([1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1])
pixels.append([1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1])
pixels.append([1, 1, 2, 3, 3, 3, 3, 3, 2, 2, 1, 1])
pixels.append([0, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1, 0])
pixels.append([0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0])
pixels.append([0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0])
pixels.append([1, 3, 1, 2, 2, 4, 2, 2, 2, 1, 3, 1])
pixels.append([1, 3, 1, 2, 2, 2, 2, 2, 2, 1, 3, 1])
pixels.append([1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1])
pixels.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
pixels.append([0, 0, 1, 2, 3, 2, 2, 3, 2, 1, 0, 0])
pixels.append([0, 0, 1, 2, 2, 1, 1, 2, 2, 1, 0, 0])
pixels.append([0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0])

for i in range(0, len(pixels)):
    for j in range(0, len(pixels[i])):
        myPen.color(colourPalette[pixels[i][j]])
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

time.sleep(15) # Pauses program for 15 seconds
