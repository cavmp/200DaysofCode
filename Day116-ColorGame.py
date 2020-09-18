import tkinter
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

timeleft = 30


def startGame(event):
    if timeleft == 30:
        countdown()

    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft > 0:

        # makes the text entry box active
        e.focus_set()

        # if the colour typed matches the colour of the text
        if e.get().lower() == colours[1].lower():
            score += 1

        # clears the text entry box when countdown is over
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))

        # update score
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time left: "
                              + str(timeleft))

        timeLabel.after(1000, countdown)

root = tkinter.Tk()

root.title("Color Game")

root.geometry("475x300")

instructions = tkinter.Label(root, text="\nType in the color"
                                        " of the words!",
                             font=('Helvetica', 20))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Type 'enter' to start",
                           font=('Helvetica', 15))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="\nTime left: " +
                                     str(timeleft), font=('Helvetica', 15))

timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()
