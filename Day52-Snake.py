import turtle as t
import time
import random

delay = 0.1
score = 0
high_score = 0

# set up the window
win = t.Screen()
win.title('Snake')
win.bgcolor('#f6cd61')
win.setup(width=600, height=600)
win.tracer(0)

# create snake head
head = t.Turtle()
head.speed(0)
head.shape('square')
head.color('#0e9aa7')
head.penup()
head.goto(0, 100)
head.direction = 'stop'

# snake food
food = t.Turtle()
food.speed(0)
food.shape('circle')
food.color('#fe8a71')
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

segments =[]

pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#4a4e4d")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("ms serif", 24))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

# move the snake
def move():
    if head.direction == 'up': # if head goes up, 'y' coordinate is increased
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down': # if head goes down, the 'y' coordinate decreases
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'right': # if head moves right, the 'x' coordinate increases
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == 'left': # if head moves left, the 'x' coordinate decreases
        x = head.xcor()
        head.setx(x - 20)

# keyboard bindings
win.listen()  # listens to key presses
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

# main game loop
while True:
    win.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        score = 0
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('ms serif', 24))
    if head.distance(food) < 15:
        # move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#3da4ab")
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
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    # Check for collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        score = 0
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('ms serif', 24))
        for segment in segments:
            segment.goto(1000, 1000)
        # clear segment list
        segments.clear()

    for segment in segments:
        if segment.distance(head) < 20:
            score = 0
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('ms serif', 24))
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            # clear segment list
            segments.clear()
    time.sleep(delay)
