from turtle import *

screen = Screen()
screenMinX = -screen.window_width() / 2
screenMinY = -screen.window_height() / 2
screenMaxX = screen.window_width() / 2
screenMaxY = screen.window_height() / 2

screen.setworldcoordinates(screenMinX, screenMinY, screenMaxX, screenMaxY)

brush_turtle = Turtle()
brush_turtle.goto(0, 0)

def on_screen_click(x, y):
    if y < screenMaxY - 40:  # only draw if clicked below color squares
        brush_turtle.speed(0)
        brush_turtle.goto(x, y)

class ColorPicker(Turtle):
    def __init__(self, color="red", num=0):
        Turtle.__init__(self)
        self.num = num
        self.color_name = color
        self.speed(0)
        self.shape("square")
        self.color("black", color)
        self.penup()

        self.onclick(lambda x, y: self.handle_click(x, y))

    def draw(self):
        self.setx(screenMinX + 110 + self.num * 30)
        self.sety(screenMaxY - 20)

    def handle_click(self, x, y):
        if self.color_name == "#F9F9F9":
            brush_turtle.penup()
            brush_turtle.color("black")
        else:
            brush_turtle.pendown()
            brush_turtle.color(self.color_name)

screen.tracer(0)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "#F9F9F9"]
color_pickers = [ColorPicker(color=c, num=i) for i, c in enumerate(colors)]
for picker in color_pickers:
    picker.draw()

while True:
    screen.onclick(on_screen_click)

    ui_turtle = Turtle()
    ui_turtle.ht()
    ui_turtle.penup()
    ui_turtle.goto(screenMinX, screenMaxY - 23)
    ui_turtle.write("Turtle Draw!", align="left", font=("Courier", 13, "bold"))

    # Resume animations now that main interface has been drawn
    screen.tracer(1)
