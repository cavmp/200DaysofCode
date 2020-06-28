from tkinter import *

class HabitTracker(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('Habit Tracker')
        self.root.geometry('750x700')

        self.label1 = Label(self.root, text='Habit Tracker\n', font=('times new roman', 45))
        self.label1.grid(row=0, column=0)

        self.days_frame = Frame(self.root)
        self.days_frame.grid(row=1, column=1)
        self.mon_label = Label(self.days_frame, text='MON', font=('times new roman', 15))
        self.tue_label = Label(self.days_frame, text='TUE', font=('times new roman', 15))
        self.wed_label = Label(self.days_frame, text='WED', font=('times new roman', 15))
        self.thu_label = Label(self.days_frame, text='THU', font=('times new roman', 15))
        self.fri_label = Label(self.days_frame, text='FRI', font=('times new roman', 15))
        self.sat_label = Label(self.days_frame, text='SAT', font=('times new roman', 15))
        self.sun_label = Label(self.days_frame, text='SUN', font=('times new roman', 15))
        self.sun_label.grid(row=1, column=3)
        self.sat_label.grid(row=1, column=4)
        self.fri_label.grid(row=1, column=5)
        self.thu_label.grid(row=1, column=6)
        self.wed_label.grid(row=1, column=7)
        self.tue_label.grid(row=1, column=8)
        self.mon_label.grid(row=1, column=9)

        self.habit_frame = Frame(self.root)
        self.habit_frame.grid(row=1, column=0)

        Checkbutton(self.days_frame) .grid(row=2, column=3)
        Checkbutton(self.days_frame) .grid(row=2, column=4)
        Checkbutton(self.days_frame) .grid(row=2, column=5)
        Checkbutton(self.days_frame) .grid(row=2, column=6)
        Checkbutton(self.days_frame) .grid(row=2, column=7)
        Checkbutton(self.days_frame) .grid(row=2, column=8)
        Checkbutton(self.days_frame) .grid(row=2, column=9)

        self.habit = Entry(self.habit_frame, width=10)
        self.habit.grid(row=1, column=0)
        self.habit_button = Button(self.habit_frame, text='ENTER', command=self.enter1)
        self.habit_button.grid(row=1, column=1)

        self.add_button = Button(self.root, text='Add another daily habit',
                                 font=('times new roman', 15), command=self.add_habit1)
        self.add_button.grid(column=1)

        mainloop()

    def enter1(self):
        text = self.habit.get()
        self.habit.destroy()
        self.habit_button.destroy()
        self.habit_label = Label(self.days_frame, text=text)
        self.habit_label.grid(row=2, column=0)

    def enter2(self):
        text = self.habit.get()
        self.habit.destroy()
        self.habit_button.destroy()
        self.habit_label = Label(self.days_frame, text=text)
        self.habit_label.grid(row=3, column=0)

    def enter3(self):
        text = self.habit.get()
        self.habit.destroy()
        self.habit_button.destroy()
        self.habit_label = Label(self.days_frame, text=text)
        self.habit_label.grid(row=4, column=0)

    def enter4(self):
        text = self.habit.get()
        self.habit.destroy()
        self.habit_button.destroy()
        self.habit_label = Label(self.days_frame, text=text)
        self.habit_label.grid(row=5, column=0)

    def enter5(self):
        text = self.habit.get()
        self.habit.destroy()
        self.habit_button.destroy()
        self.habit_label = Label(self.days_frame, text=text)
        self.habit_label.grid(row=6, column=0)
    
    def enter6(self):
        text = self.habit.get()
        self.habit.destroy()
        self.habit_button.destroy()
        self.habit_label = Label(self.days_frame, text=text)
        self.habit_label.grid(row=7, column=0)

    def enter7(self):
        text = self.habit.get()
        self.habit.destroy()
        self.habit_button.destroy()
        self.habit_label = Label(self.days_frame, text=text)
        self.habit_label.grid(row=8, column=0)

    def add_habit1(self):
        Checkbutton(self.days_frame).grid(row=3, column=3)
        Checkbutton(self.days_frame).grid(row=3, column=4)
        Checkbutton(self.days_frame).grid(row=3, column=5)
        Checkbutton(self.days_frame).grid(row=3, column=6)
        Checkbutton(self.days_frame).grid(row=3, column=7)
        Checkbutton(self.days_frame).grid(row=3, column=8)
        Checkbutton(self.days_frame).grid(row=3, column=9)

        self.habit_frame = Frame(self.root)
        self.habit_frame.grid(row=2, column=0)
        self.habit = Entry(self.habit_frame, width=10)
        self.habit.grid(row=2, column=0)
        self.habit_button = Button(self.habit_frame, text='ENTER', command=self.enter2)
        self.habit_button.grid(row=2, column=1)
        self.add_button.destroy()
        self.add_button = Button(self.root, text='Add another daily habit',
                                 font=('times new roman', 15), command=self.add_habit2)
        self.add_button.grid(column=1)
        
    

    def add_habit2(self):
        Checkbutton(self.days_frame).grid(row=4, column=3)
        Checkbutton(self.days_frame).grid(row=4, column=4)
        Checkbutton(self.days_frame).grid(row=4, column=5)
        Checkbutton(self.days_frame).grid(row=4, column=6)
        Checkbutton(self.days_frame).grid(row=4, column=7)
        Checkbutton(self.days_frame).grid(row=4, column=8)
        Checkbutton(self.days_frame).grid(row=4, column=9)

        self.habit_frame = Frame(self.root)
        self.habit_frame.grid(row=3, column=0)
        self.habit = Entry(self.habit_frame, width=10)
        self.habit.grid(row=3, column=0)
        self.habit_button = Button(self.habit_frame, text='ENTER', command=self.enter3)
        self.habit_button.grid(row=3, column=1)
        self.add_button.destroy()
        self.add_button = Button(self.root, text='Add another daily habit',
                                 font=('times new roman', 15), command=self.add_habit3)
        self.add_button.grid(column=1)

    def add_habit3(self):
        Checkbutton(self.days_frame).grid(row=5, column=3)
        Checkbutton(self.days_frame).grid(row=5, column=4)
        Checkbutton(self.days_frame).grid(row=5, column=5)
        Checkbutton(self.days_frame).grid(row=5, column=6)
        Checkbutton(self.days_frame).grid(row=5, column=7)
        Checkbutton(self.days_frame).grid(row=5, column=8)
        Checkbutton(self.days_frame).grid(row=5, column=9)

        self.habit_frame = Frame(self.root)
        self.habit_frame.grid(row=4, column=0)
        self.habit = Entry(self.habit_frame, width=10)
        self.habit.grid(row=4, column=0)
        self.habit_button = Button(self.habit_frame, text='ENTER', command=self.enter4)
        self.habit_button.grid(row=4, column=1)
        self.add_button.destroy()
        self.add_button = Button(self.root, text='Add another daily habit',
                                 font=('times new roman', 15), command=self.add_habit4)
        self.add_button.grid(column=1)

    def add_habit4(self):
        Checkbutton(self.days_frame).grid(row=6, column=3)
        Checkbutton(self.days_frame).grid(row=6, column=4)
        Checkbutton(self.days_frame).grid(row=6, column=5)
        Checkbutton(self.days_frame).grid(row=6, column=6)
        Checkbutton(self.days_frame).grid(row=6, column=7)
        Checkbutton(self.days_frame).grid(row=6, column=8)
        Checkbutton(self.days_frame).grid(row=6, column=9)

        self.habit_frame = Frame(self.root)
        self.habit_frame.grid(row=5, column=0)
        self.habit = Entry(self.habit_frame, width=10)
        self.habit.grid(row=5, column=0)
        self.habit_button = Button(self.habit_frame, text='ENTER', command=self.enter5)
        self.habit_button.grid(row=5, column=1)
        self.add_button.destroy()
        self.add_button = Button(self.root, text='Add another daily habit',
                                 font=('times new roman', 15), command=self.add_habit5)
        self.add_button.grid(column=1)

    def add_habit5(self):
        Checkbutton(self.days_frame).grid(row=7, column=3)
        Checkbutton(self.days_frame).grid(row=7, column=4)
        Checkbutton(self.days_frame).grid(row=7, column=5)
        Checkbutton(self.days_frame).grid(row=7, column=6)
        Checkbutton(self.days_frame).grid(row=7, column=7)
        Checkbutton(self.days_frame).grid(row=7, column=8)
        Checkbutton(self.days_frame).grid(row=7, column=9)

        self.habit_frame = Frame(self.root)
        self.habit_frame.grid(row=6, column=0)
        self.habit = Entry(self.habit_frame, width=10)
        self.habit.grid(row=6, column=0)
        self.habit_button = Button(self.habit_frame, text='ENTER', command=self.enter6)
        self.habit_button.grid(row=6, column=1)
        self.add_button.destroy()
        self.add_button = Button(self.root, text='Add another daily habit',
                                 font=('times new roman', 15), command=self.add_habit6)
        self.add_button.grid(column=1)

    def add_habit6(self):
        Checkbutton(self.days_frame).grid(row=8, column=3)
        Checkbutton(self.days_frame).grid(row=8, column=4)
        Checkbutton(self.days_frame).grid(row=8, column=5)
        Checkbutton(self.days_frame).grid(row=8, column=6)
        Checkbutton(self.days_frame).grid(row=8, column=7)
        Checkbutton(self.days_frame).grid(row=8, column=8)
        Checkbutton(self.days_frame).grid(row=8, column=9)

        self.habit_frame = Frame(self.root)
        self.habit_frame.grid(row=7, column=0)
        self.habit = Entry(self.habit_frame, width=10)
        self.habit.grid(row=7, column=0)
        self.habit_button = Button(self.habit_frame, text='ENTER', command=self.enter7)
        self.habit_button.grid(row=7, column=1)
        self.add_button.destroy()


if __name__ == '__main__':
    HabitTracker()
