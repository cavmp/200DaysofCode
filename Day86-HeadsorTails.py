from tkinter import *
from PIL import ImageTk, Image
import random

class HeadsorTails(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('Heads or Tails')
        self.root.geometry('600x700')

        self.question_lbl = Label(self.root, text='Heads or Tails?', font=('Arial 30 bold'))
        self.question_lbl.pack(pady=40)

        self.heads_btn = Button(self.root, text='FLIP COIN', command=self.flip_coin)
        self.heads_btn.pack(pady=30)

        self.frame = Frame(self.root)
        self.frame.pack(side=TOP)

        image = Image.open('images/coinflip.png')
        self.image = image.resize((300, 300), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.pic = Label(self.frame, image=self.image)
        self.pic.pack(side=TOP)

        self.frame1 = Frame(self.root)
        self.frame1.pack(side=TOP)
        self.lbl1 = Label(self.frame1, font=('Arial 20'), text='You got:')
        self.lbl1.pack(side=LEFT)
        self.lbl2 = Label(self.frame1, font=('Arial 20'))
        self.lbl2.pack(side=LEFT)

        self.root.mainloop()

    def flip_coin(self):
        rand_num = random.randint(1, 2)
        if rand_num == 1:
            self.pic.destroy()
            image = Image.open('images/heads.png')
            self.image = image.resize((300, 300), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image)
            self.pic = Label(self.frame, image=self.image)
            self.pic.pack(side=TOP)
            self.lbl2.configure(text="HEADS")
        if rand_num == 2:
            self.pic.destroy()
            image = Image.open('images/tails.png')
            self.image = image.resize((300, 300), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image)
            self.pic = Label(self.frame, image=self.image)
            self.pic.pack(side=TOP)
            self.lbl2.configure(text="TAILS")

if __name__ == '__main__':
    HeadsorTails()
