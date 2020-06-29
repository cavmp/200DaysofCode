import tkinter
import time

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels

# Constants for the ball and paddle
BALL_SIZE = 20
PADDLE_Y = CANVAS_WIDTH - 30
PADDLE_X = 10

score = 0

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Pong')

    x = CANVAS_WIDTH / 2
    ball = canvas.create_oval(x, 400, x + BALL_SIZE, BALL_SIZE + 400, fill='green', outline='green')
    paddle = canvas.create_rectangle(0, PADDLE_Y, 10, PADDLE_Y + 90, fill='blue')
    paddle1 = canvas.create_rectangle(0, PADDLE_Y, 10, PADDLE_Y + 90, fill='red')

    start_text = canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, fill='blue', font="System 30",
                                    text='Click to start!')

    while start_text in canvas.find_all():
        canvas.bind("<ButtonRelease-1>", lambda e: canvas.delete(start_text))
        canvas.update()
        time.sleep(1 / 10.)

    dx = 10
    dy = 10
    while True:
        mouse_y = canvas.winfo_pointery()
        canvas.moveto(paddle, PADDLE_X, mouse_y)
        canvas.moveto(paddle1, PADDLE_Y, mouse_y)

        canvas.move(ball, dx, dy)
        if hit_top_wall(canvas, ball) or hit_bottom_wall(canvas, ball):
            dy *= -1

        if hit_paddle(canvas, ball, paddle) or hit_paddle1(canvas, ball, paddle1):
            dx *= -1
            global score
            score += 1
            canvas.create_rectangle(290, 6, 320, 36, fill='black')
            canvas.create_text(305, 20, font='System 20', text=score, fill='white')

        canvas.update()
        time.sleep(1/30.)

        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            canvas.create_text(305, 390, font='System 40', text='GAME OVER')
            text = "You scored: ",score
            canvas.create_text(305, 420, font='System, 20', text=text)

def hit_paddle(canvas, ball, paddle):
    paddle_coords = canvas.coords(paddle)
    x1 = paddle_coords[0]
    y1 = paddle_coords[1]
    x2 = paddle_coords[2]
    y2 = paddle_coords[3]
    results = canvas.find_overlapping(x1, y1, x2, y2)
    return len(results) > 1

def hit_paddle1(canvas, ball, paddle1):
    paddle_coords = canvas.coords(paddle1)
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
    return get_bottom_y(canvas,object) >= CANVAS_HEIGHT

def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]

def make_canvas(width, height, title):
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()

