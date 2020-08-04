from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.title('Roll Dice')

# Label for the dice
label = Label(root, text='', font=('Helvetica', 260))

# Rolls the dice
def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] # unicode character strings for dice
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.pack(side=TOP, pady=0)

# Button to roll the dice
button = Button(root, text='Roll Dice', command=roll_dice)
button.pack(side=BOTTOM, pady=10)

root.mainloop()
