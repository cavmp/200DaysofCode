from tkinter import *
from playsound import playsound
from PIL import ImageTk
from PIL import Image

class MomentofPeace(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('Moment of Calm')
        self.root.geometry('1025x750')
        self.root.configure(background='steelblue')

        self.mop_label = Label(self.root, font=('times new roman', 45, 'italic', 'bold'), fg='white',
                               bg='steelblue', text='A Moment of Calm')
        self.mop_label.pack(side=TOP)

        self.instructions_label = Label(self.root, text='\nWelcome to your daily calm. Turn off your phone, put on your'
                                                        ' headphones, and take a moment alone with yourself.',
                                        fg='white', font=('times new roman', 20), bg='steelblue')
        self.instructions_label.pack(side=TOP)

        self.options_label = Label(self.root, font=('times new roman', 20), text='How long would you like your moment'
                                                                                 ' to be?\n', bg='steelblue', fg='white')
        self.options_label.pack(side=TOP)

        self.button_frame = Frame(self.root)
        self.button_frame.pack(side=TOP)

        self.twomin_button = Button(self.button_frame, font=('ms serif', 20), text='2 MINS',
                                    bg='white', fg='steelblue', command=self.twomin)
        self.twomin_button.pack(side=LEFT)

        self.fivemin_button = Button(self.button_frame, font=('ms serif', 20), text='5 MINS',
                                     bg='white', fg='steelblue', command=self.fivemin)
        self.fivemin_button.pack(side=LEFT)

        self.tenmin_button = Button(self.button_frame, font=('ms serif', 20), text='10 MINS',
                                    bg='white', fg='steelblue', command=self.tenmin)
        self.tenmin_button.pack(side=LEFT)

        self.fifteenmin_button = Button(self.button_frame, font=('ms serif', 20), bg='white',
                                        fg='steelblue', text='15 MINS', command=self.fifteenmin)
        self.fifteenmin_button.pack(side=LEFT)

        self.twentymin_button = Button(self.button_frame, font=('ms serif', 20), bg='white',
                                       fg='steelblue', text='20 MINS', command=self.twentymin)
        self.twentymin_button.pack(side=LEFT)

        self.image = ImageTk.PhotoImage(Image.open('images/calm.jpg'))
        self.pic = Label(self.root, image=self.image)
        self.pic.pack(side=BOTTOM, expand=YES)

        self.root.mainloop()

    def twomin(self):
        playsound('music/2mins.mp3')

    def fivemin(self):
        playsound('music/5mins.mp3')

    def tenmin(self):
        playsound('music/10mins.mp3')

    def fifteenmin(self):
        playsound('music/15mins.mp3')

    def twentymin(self):
        playsound('music/20mins.mp3')

if __name__ == '__main__':
    MomentofPeace()
