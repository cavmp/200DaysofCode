import random
from tkinter import *

class RandomNumbers(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('Random Numbers')
        self.root.geometry('825x550')

        self.mop_label = Label(self.root, font=('times new roman', 30), text='Random Numbers\n')
        self.mop_label.pack(side=TOP)

        self.frame1 = Frame(self.root)
        self.frame1.pack(side=TOP)
        self.quantity_label = Label(self.frame1, text='How many numbers do you need? ')
        self.quantity_label.pack(side=LEFT)
        self.quantity_entry = Entry(self.frame1, width=5)
        self.quantity_entry.pack(side=LEFT)

        self.frame2 = Frame(self.root)
        self.frame2.pack(side=TOP)
        self.min_label = Label(self.frame2, text='Minimum number: ')
        self.min_label.pack(side=LEFT)
        self.min_entry = Entry(self.frame2, width=3)
        self.min_entry.pack(side=LEFT)
        self.max_label = Label(self.frame2, text='Maximum number: ')
        self.max_label.pack(side=LEFT)
        self.max_entry = Entry(self.frame2, width=3)
        self.max_entry.pack(side=LEFT)

        self.frame3 = Frame(self.root)
        self.frame3.pack(side=TOP)
        Label(self.frame3, text='\n') .pack(side=TOP)
        self.results_button = Button(text='Click to get your random numbers: ', command=self.randomnum)
        self.results_button.pack(side=TOP)

        self.root.mainloop()

    def randomnum(self):

        quantity = self.quantity_entry.get()
        min = self.min_entry.get()
        max = self.max_entry.get()

        for i in range(int(quantity)):
            random_number = random.randint(int(min), int(max))
            self.results = Label(self.frame3, text=random_number)
            self.results.pack(side=TOP)
            self.results_button.destroy()


if __name__ == '__main__':
    RandomNumbers()
