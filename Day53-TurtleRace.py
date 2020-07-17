import turtle as t
from turtle import Turtle
import time
from random import randint

# set up window
window = t.Screen()
window.title('Turtle Race')
t.bgcolor('#7bc043') # green field
t.speed(0)
t.penup()
t.setpos(-140, 200)
t.color('white')
t.write("TURTLE RACE", font=("Arial", 30, "bold"))
t.penup()

# dirt
t.setpos(-400, -180)
t.color('#4f372d')
t.begin_fill()
t.pendown()
t.forward(800) # draw 800 pixels going forward
t.right(90) # same logic as this ^
t.forward(300)
t.right(90)
t.forward(800)
t.right(90)
t.forward(300)
t.end_fill()

# finish line
stamp_size = 20
square_size = 15
finish_line = 200

t.color('black')
t.shape('square')
t.shapesize(square_size / stamp_size)
t.penup()

for i in range(10):
    t.setpos(finish_line, (150 - (i * square_size * 2)))
    t.stamp()

for j in range(10):
    t.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    t.stamp()

t.hideturtle()

turtles = []
turt_colours = ["#edc951", "#eb6841", "#cc2a36", "#00a0b0"]
for i in range(4):
    t = Turtle()
    t.speed(0)
    t.color(turt_colours[i])
    t.shape("turtle")
    t.penup()
    t.goto(-250, 100 - i * 50)
    t.pendown()
    turtles.append(t)

def race():
    # MOVE TURTLES
    win = False
    while not win:
        for index, t in enumerate(turtles):
            t.forward(randint(1, 5))
            if t.xcor() >= 200:
                print('The winner is turtle #', index + 1, "!")
                win = True
                t.speed(1)
                t.right(270)  # Victory spin

                break


def main():
    countdown = 3  # Countdown from this number to 1
    for k in range(1, countdown + 1):
        print(countdown + 1 - k)
        time.sleep(1)  # Pause for 1 second
    print("Go!")

    race()

    print("End")
    window.mainloop()


main()
