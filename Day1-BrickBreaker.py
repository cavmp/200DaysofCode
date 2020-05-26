"""
File: brickbreaker.py
----------------
This is the classic 'breakout' game. This was my final project for my first ever coding course online. I had a hard time
figuring out how to do it at first but actually was able to accomplish it. The feeling after accomplishing this was really amazing!
"""

from flask import Flask
import tkinter
import time
import random
import math
import numpy as np

# How big is the playing area?
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 8              # How many rows of bricks are there?
N_COLS = 10             # How many columns of bricks are there?
SPACING = 5             # How much space is there between each brick?
BRICK_START_Y = 50      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS+1) * SPACING) / N_COLS

# Constants for the ball and paddle
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Brick Breaker')
    for row in range(N_ROWS):
        for col in range(N_COLS):
            bricks(canvas, row, col)

    x = CANVAS_WIDTH / 2
    ball = canvas.create_oval(x, 400, x + BALL_SIZE, BALL_SIZE + 400, fill='black', outline='black')
    paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, CANVAS_HEIGHT - 20, fill='black')

    dx = 10
    dy = 10
    while True:
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle, mouse_x, PADDLE_Y)

        canvas.move(ball, dx, dy)
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1
        if hit_top_wall(canvas, ball):
            dy *= -1

        if hit_paddle(canvas, ball, paddle):
            dy *= -1
        if hit_bricks(canvas, ball, paddle):
            dy *= -1

        canvas.update()
        time.sleep(1/50.)


def bricks(canvas, row, col):
    x = (BRICK_WIDTH + SPACING) * col
    y = (BRICK_HEIGHT + SPACING) * row
    color = get_color(row)
    canvas.create_rectangle(x + BRICK_WIDTH, y + BRICK_HEIGHT, x, y, fill=color, outline=color)


def get_color(row):
    if row == 0:
        return'red'
    if row == 1:
        return'orange'
    if row == 2:
        return 'yellow'
    if row == 3:
        return 'greenyellow'
    if row == 4:
        return 'green'
    if row == 5:
        return 'cyan'
    if row == 6:
        return 'blue'
    if row == 7:
        return 'purple'

def hit_bricks(canvas, ball, paddle):
    ball_coords = canvas.coords(ball)
    x1 = ball_coords[0]
    y1 = ball_coords[1]
    x2 = ball_coords[2]
    y2 = ball_coords[3]
    colliding_list = canvas.find_overlapping(x1, y1, x2, y2)
    for objects in colliding_list:
        if objects == ball or objects == paddle:
            return len(colliding_list) > 2
        else:
            canvas.delete(objects)
            return len(colliding_list) > 1

def hit_paddle(canvas, ball, paddle):
    paddle_coords = canvas.coords(paddle)
    x1 = paddle_coords[0]
    y1 = paddle_coords[1]
    x2 = paddle_coords[2]
    y2 = paddle_coords[3]
    results = canvas.find_overlapping(x1, y1, x2, y2)
    return len(results) > 1

def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0

def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0

def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH

def hit_bottom_wall(canvas, object):
    return get_bottom_y() >= CANVAS_HEIGHT

def get_left_x(canvas, object):
    '''
    This friendly method returns the x coordinate of the left of an object.
    Recall that canvas.coords(object) returns a list of the object
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 0 is the left-x
    '''
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    '''
    This friendly method returns the y coordinate of the top of an object.
    Recall that canvas.coords(object) returns a list of the object 
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 1 is the top-y
    '''
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]

def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()
