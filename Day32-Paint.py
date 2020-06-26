from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('Paint')

        self.canvas = Canvas(self.root, bg='white', width=800, height=700)
        self.canvas.grid(row=2, columnspan=5)

        self.pen_button = Button(self.root, text='PEN', command=self.pen)
        self.pen_button.grid(row=1, column=0)

        self.brush_button = Button(self.root, text='BRUSH', command=self.brush)
        self.brush_button.grid(row=1, column=1)

        self.color_button = Button(self.root, text='COLOR', command=self.choose_color)
        self.color_button.grid(row=1, column=2)

        self.eraser_button = Button(self.root, text='ERASER', command=self.eraser)
        self.eraser_button.grid(row=1, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=100, orient=VERTICAL)
        self.choose_size_button.grid(row=1, column=4)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.line_width = self.choose_size_button.get()
        self.color = 'black' # default color
        self.eraser_on = False
        self.active_button = self.pen_button
        self.canvas.bind('<B1-Motion>', self.paint)

    def pen(self):
        self.activate_button(self.pen_button)

    def brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        x1, y1 = (event.x-1), (event.y-1)
        x2, y2 = (event.x+1), (event.y+1)
        self.canvas.create_line(x1, y1, x2, y2, width=self.line_width, fill=paint_color, capstyle=ROUND, smooth=TRUE)

if __name__ == '__main__':
    Paint()
