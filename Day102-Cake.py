import turtle
import math
import time

myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(0)
myPen.hideturtle()
window = turtle.Screen()
window.bgcolor("#69D9FF")
y = -140

ingredients = {}

ingredients["vanilla"]="#f3e5ab"
ingredients["pistachio"]="#7DFA7F"
ingredients["raspberry"]="#e30b5d"
ingredients["strawberry"]="#FF0D0D"
ingredients["cherry"]="#C20067"
ingredients["apricot"]="#FFB300"
ingredients["lemon"]="#FFFA5C"
ingredients["kiwi"]="#67F55F"
ingredients["pineapple"]="#FFFF17"
ingredients["mango"]="#FFE838"
ingredients["mint"]="#5FF5A0"
ingredients["white chocolate"]="#FFFDC4"
ingredients["milk chocolate"]="#BF671F"
ingredients["dark chocolate"]="#2A1506"
ingredients["coffee"]="#d2691e"
ingredients["toffee"]="#E35209"
ingredients["mocha"]="#93c572"
ingredients["icing sugar"]="#FFFFFF"

#Initialise the list of layers
layers = []
#Add values to the list
layers.append(["raspberry",30])
layers.append(["dark chocolate",20])
layers.append(["milk chocolate",40])
layers.append(["mango",60])
#Add more layers...

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
    turtle.hideturtle()
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
    turtle.getscreen().update()


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
    turtle.getscreen().update()


def addCherry(turtle, color, x, y, radius):
    draw_circle(turtle, color, x, y, radius)
    turtle.getscreen().update()


def addIcing(turtle, color, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(-125, y + 10)
    turtle.pendown()
    turtle.begin_fill()

    for x in range(-125, 125):
        turtle.goto(x, y - 10 - 10 * math.cos((x / 100) * 2 * math.pi))

    turtle.goto(125, y + 10)
    turtle.goto(-125, y + 10)
    turtle.end_fill()
    turtle.getscreen().update()

#Preview the content of the list
print(layers)

#Plate
draw_rectangle(turtle, "white", -150, y-10, +300, 10)


#Iterate through each layer of the list
for layer in layers:
  draw_rectangle(myPen, ingredients[layer[0]], -120, y, 240, layer[1])
  y+=layer[1]

addIcing(myPen, ingredients["icing sugar"],y)
addCherry(myPen, ingredients["cherry"], 0, y+10, 15)

myPen.getscreen().update()

time.sleep(10)
