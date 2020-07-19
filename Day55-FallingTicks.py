import turtle
import random
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Falling Ticks")
wn.bgcolor("black")
wn.bgpic("images/background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("images/doggo.gif")

# Score
score = 0

# Health
lives = 3

# Player
player = turtle.Turtle()
player.speed(0)
player.shape("images/doggo.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Dog food
dog_foods = []

for _ in range(20):
    dog_food = turtle.Turtle()
    dog_food.speed(0)
    dog_food.shape("circle")
    dog_food.color("#8d5524")
    dog_food.penup()
    dog_food.goto(-100, 250)
    dog_food.speed = random.randint(1, 2)

    dog_foods.append(dog_food)

# ticks
ticks = []

for _ in range(20):
    tick = turtle.Turtle()
    tick.speed(0)
    tick.shape("turtle")
    tick.color("black")
    tick.penup()
    tick.goto(100, 250)
    tick.speed = random.randint(1, 2)

    ticks.append(tick)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("images/doggo.gif")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 24, "normal"))


# Functions
def go_left():
    player.direction = "left"
    player.shape("images/doggo.gif")


def go_right():
    player.direction = "right"
    player.shape("images/doggo.gif")


# Keyboard bindings
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Move the player
    if player.direction == "left":
        player.setx(player.xcor() - 1)

    if player.direction == "right":
        player.setx(player.xcor() + 1)

    # Check for border collisions
    if player.xcor() < -390:
        player.setx(-390)

    elif player.xcor() > 390:
        player.setx(390)

    for dog_food in dog_foods:
        # Move the dog food
        dog_food.sety(dog_food.ycor() - dog_food.speed)

        # Check if dog foods are off the screen
        if dog_food.ycor() < -300:
            dog_food.goto(random.randint(-300, 300), random.randint(400, 800))

        # Check for collisions
        if player.distance(dog_food) < 40:
            # Score increases
            score += 10

            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

            # Move the dog food back to the top
            dog_food.goto(random.randint(-300, 300), random.randint(400, 800))

    for tick in ticks:
        # Move the bad things
        tick.sety(tick.ycor() - tick.speed)

        if tick.ycor() < -300:
            tick.goto(random.randint(-300, 300), random.randint(400, 800))

        if player.distance(tick) < 40:
            # Score increases
            score -= 10
            lives -= 1

            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

            time.sleep(1)
            # Move the bad things back to the top
            for tick in ticks:
                tick.goto(random.randint(-300, 300), random.randint(400, 800))

    # Check for game over
    if lives == 0:
        pen.clear()
        pen.write("Game Over! Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        wn.update()
        time.sleep(5)
        score = 0
        lives = 3
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
