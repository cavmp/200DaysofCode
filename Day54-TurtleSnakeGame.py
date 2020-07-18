import turtle as t
from turtle import Turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# set up window
win = t.Screen()
win.title('Turtle Snake')
t.bgcolor('#008744') # green field
t.speed(0)

# snake food
food = t.Turtle()
food.speed(0)
food.shape('circle')
food.color('#ffffff')
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

segments =[]

t = Turtle()
t.speed(0)
t.color('#ffa700')
t.shape("turtle")
t.penup()
t.goto(0, 100)
t.pendown()
t.direction = 'stop'

pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("ms serif", 24))

def go_up():
    if t.direction != "down":
        t.direction = "up"

def go_down():
    if t.direction != "up":
        t.direction = "down"

def go_right():
    if t.direction != "left":
        t.direction = "right"

def go_left():
    if t.direction != "right":
        t.direction = "left"

# move the snake
def move():
    if t.direction == 'up': # if t goes up, 'y' coordinate is increased
        y = t.ycor()
        t.sety(y + 20)

    if t.direction == 'down': # if t goes down, the 'y' coordinate decreases
        y = t.ycor()
        t.sety(y - 20)

    if t.direction == 'right': # if t moves right, the 'x' coordinate increases
        x = t.xcor()
        t.setx(x + 20)

    if t.direction == 'left': # if t moves left, the 'x' coordinate decreases
        x = t.xcor()
        t.setx(x - 20)

# keyboard bindings
win.listen()  # listens to key presses
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

# main game loop
while True:
    win.update()
    if t.xcor() > 290 or t.xcor() < -290 or t.ycor() > 290 or t.ycor() < -290:
        score = 0
        time.sleep(1)
        t.goto(0, 0)
        t.direction = "stop"
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('ms serif', 24))

    if t.distance(food) < 15:
        # move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        colors = ['#0057e7', '#d62d20', '#ffa700']
        num = random.randrange(len(colors))
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("turtle")
        new_segment.color(colors[num])
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        delay -= 0.001
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('ms serif', 24))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = t.xcor()
        y = t.ycor()
        segments[0].goto(x, y)
    move()

    # Check for collision
    if t.xcor() > 290 or t.xcor() < -290 or t.ycor() > 290 or t.ycor() < -290:
        score = 0
        time.sleep(1)
        t.goto(0, 0)
        t.direction = "stop"
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('ms serif', 24))
        for segment in segments:
            segment.goto(1000, 1000)
        # clear segment list
        segments.clear()

    for segment in segments:
        if segment.distance(t) < 20:
            score = 0
            time.sleep(1)
            t.goto(0, 0)
            t.direction = "stop"
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('ms serif', 24))
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            # clear segment list
            segments.clear()
    time.sleep(delay)

main()
