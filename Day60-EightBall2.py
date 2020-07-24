from tkinter import *
from PIL import ImageTk
from PIL import Image
import random

class EightBall(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('Eight Ball')
        self.root.geometry('700x500')

        self.space = Label(self.root, text='\n\n\n\n') # To add a space in between
        self.space.pack(side=TOP)

        self.image = ImageTk.PhotoImage(Image.open('images/8ball.png'))
        self.pic = Label(self.root, image=self.image)
        self.pic.pack(side=TOP)

        self.f1 = Frame(self.root)
        self.f1.pack(side=BOTTOM)
        self.entry = Entry(self.f1, font =("Verdana", 16)) .pack(side=LEFT)
        self.button = Button(self.f1, font=('Verdana', 16), text='Ask', command=self.random_ans) .pack(side=LEFT)

        self.root.mainloop()

    def random_ans(self):
        rand_num = random.randint(1, 5)
        if rand_num == 1:
            self.pic.destroy()
            self.image = ImageTk.PhotoImage(Image.open('images/8_answerisyes.png'))
            self.pic = Label(self.root, image=self.image)
            self.pic.pack(side=TOP)
        if rand_num == 2:
            self.pic.destroy()
            self.image = ImageTk.PhotoImage(Image.open('images/8_asklater.png'))
            self.pic = Label(self.root, image=self.image)
            self.pic.pack(side=TOP)
        if rand_num == 3:
            self.pic.destroy()
            self.image = ImageTk.PhotoImage(Image.open('images/8_no.png'))
            self.pic = Label(self.root, image=self.image)
            self.pic.pack(side=TOP)
        if rand_num == 4:
            self.pic.destroy()
            self.image = ImageTk.PhotoImage(Image.open('images/8_noidea.png'))
            self.pic = Label(self.root, image=self.image)
            self.pic.pack(side=TOP)
        if rand_num == 5:
            self.pic.destroy()
            self.image = ImageTk.PhotoImage(Image.open('images/8_yes.png'))
            self.pic = Label(self.root, image=self.image)
            self.pic.pack(side=TOP)


if __name__ == '__main__':
    EightBall()
