import turtle as t
import math
import random

# Screen
window = t.Screen()
window.title('Social Distance')
window.bgpic('images/grass.gif')
window.bgcolor('green')
window.tracer(3)

# Border
mypen = t.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.color('#5e5656')
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Player
player = t.Turtle()
player.color('red')
player.shape('triangle')
player.penup()

# Infected People
infected = 100

# Player's goals
max_goals = 20
goals = []

for count in range(max_goals):
    goals.append(t.Turtle())
    goals[count].color('white')
    goals[count].shape('triangle')
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

speed = 1

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

t.listen()
t.onkey(turnleft, 'Left')
t.onkey(turnright, 'Right')
t.onkey(increasespeed, 'Up')


while True:
    player.forward(speed)

    # Boundary
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)

    if player.ycor() > 300 or player.ycor() <-300:
        player.right(180)

    # Move the goal
    for count in range(max_goals):
        goals[count].forward(3)

        # Boundary check for goal
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)

        # Check for collisions
        if isCollision(player, goals[count]):
            goals[count].color('red')
            goals[count].right(random.randint(0, 360))
            infected -= 1
            # Draws the score on screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Number of People You Haven't Infected/ Your Score as a Responsible Citizen: %s" %infected
            mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
