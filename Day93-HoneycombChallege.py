import turtle

myPen = turtle.Turtle()
myPen.shape("arrow")

size = 20
circles = 20
myPen.speed(100)

def move(length, angle):
                myPen.right(angle)
                myPen.forward(length)

def hex():
        myPen.pendown()
        myPen.color("#a86f14")
        myPen.fillcolor("#efb456")
        myPen.begin_fill()
        for i in range(6):
                move(size,-60)
        myPen.end_fill()
        myPen.penup()

# start
myPen.penup()

for circle in range (circles):
        if circle == 0:
                hex()
                move(size,-60)
                move(size,-60)
                move(size,-60)
                move(0,180)
        for i in range (6):
                move(0,60)
                for j in range (circle+1):
                        hex()
                        move(size,-60)
                        move(size,60)
                move(-size,0)
        move(-size,60)
        move(size,-120)
        move(0,60)

myPen.exitonclick()
