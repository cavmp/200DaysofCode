import random
from tkinter import *

# Name of the file to read in!
WORD_LIST = ['Dance', 'Shark', 'Chair', 'Smile', 'Basketball', 'Volleyball', 'Kangaroo', 'Scissors', 'Alligator',
             'Monkey', 'Elephant', 'Dog', 'Cat', 'Doll', 'Balloon', 'Pig', 'Tail', 'Ear', 'Mosquito', 'Toothbrush',
             'Turtle', 'Whale', 'Wave', 'Football', 'Sneeze', 'Book', 'Spider', 'Sleep', 'Jumping Jacks', 'Bird',
             'Skip', 'Chicken', 'Robot', 'Baseball', 'Car', 'Telephone', 'Door', 'Party', 'Windmill', 'President',
             'Volcano', 'Gym', 'Business Trip', 'Mirror', 'Honk', 'Cast', 'Flamingo', 'Mouse Trap', 'Torch', 'Eraser',
             'Washing Machine', 'Gingerbread Man', 'Spider Web', 'Chess', 'Artist', 'Spine', 'Quicksand', 'Stiff',
             'Doghouse', 'Ticket', 'Cowboy', 'Sand', 'Pizza', 'Taxi', 'Skip', 'Shadow', 'Wax', 'Nightmare', 'Lawn Mower']
num = random.randrange(len(WORD_LIST))

root = Tk()
root.geometry('600x400')
root.title('Heads Up')
root.configure(background='#006494')

frame = Frame(root, bg='#e8f1f2', bd=10)
frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.6, anchor=CENTER)

label = Label(frame, text='Click to Start!', font=('Arial 30 bold'))
label.place(relwidth=1, relheight=1)

start_time = 3

def start():
    global start_time
    start_button.destroy()
    if start_time > 0:
        label.config(text=start_time)
        start_time -= 1
        label.after(1000, start)
    elif start_time == 0:
        label.config(text=0)
        play()

start_button = Button(frame, text='PLAY', command=start)
start_button.pack(side=BOTTOM)


game_time = 60
words_scored = 0

def correct():
    global words_scored
    words_scored += 1
    global num, WORD_LIST
    num = random.randrange(0, len(WORD_LIST), 1)
    label.config(text=WORD_LIST[num])

def p():
    global num, WORD_LIST
    num = random.randrange(0, len(WORD_LIST), 1)
    label.config(text=WORD_LIST[num])

button_frame = Frame(frame) # frame inside the frame
button_frame.pack(side=BOTTOM)
correct_button = Button(button_frame, text='CORRECT', relief=GROOVE, command=correct, fg='green')
pass_button = Button(button_frame, text='PASS', relief=GROOVE, command=p, fg='red')

timer_label = Label(frame)
timer_label.pack(side=BOTTOM)

def play():
    global game_time
    start_button.destroy()

    pass_button.pack(side=LEFT)
    correct_button.pack(side=LEFT)

    if game_time > 0:
        timer_label.config(text=game_time)
        game_time -= 1
        timer_label.after(1000, play)

        label.config(text=WORD_LIST[num])

    elif game_time == 0:
        timer_label.config(text=0)
        label.config(text="Words Scored: {0}".format(words_scored))

root.mainloop()
