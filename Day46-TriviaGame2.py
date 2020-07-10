from tkinter import *
import random

questions = ['Water has a pH level of around?', "What's the hardest rock?", 'What is the national dish of spain?',
             'Which horoscope sign has a crab?', 'The statue of liberty was given to US by which country?',
             'What color is absinthe?', 'What substance are nails made of?', 'When did the cold war end?',
             'Where is the Sea of Tranquility located?', 'What is the most common letter in the English alphabet?',
             'Chimpanzees and gorillas have human-like fingerprints and so do what other non-human animal?',
             'What planets literally rain diamonds', 'Saudi Arabia imports camels from what country?'
             'What is the only state that borders just one other state?', 'What is the Twitter bird’s official?',
             'What is a community of ants called?', 'Who was said to “float like a butterfly and sting like a bee”?',
             'Where did Heineken beer originate?', 'How many signs are there in the Zodiac?']
answers = ['7', 'A diamond' and 'a diamond', 'Paella' and 'paella', 'Cancer' and 'cancer', 'France' and 'france',
           'Green' and 'green', 'Keratin' and 'keratin', '1989', 'The moon' and 'the moon', 'E' and 'e', 'koalas',
           'Saturn and Jupiter', 'Australia', 'Maine', 'Larry', 'A colony', 'Muhammed Ali', 'Netherlands', '12']

score = 0

num = random.randrange(len(answers))

def default():
    global questions, answers, num
    lbl.config(text=questions[num])

def res():
    global questions, answers, num
    num = random.randrange(0, len(questions), 1)
    lbl.config(text=questions[num])
    e1.delete(0, END)

def checkans():
    global questions, answers, num, score
    var = e1.get()
    if var == answers[num]:
        score += 1
        check.config(text="\n\nCorrect!")
        scorenumlbl.config(text=score)
        res()
    else:
        score = 0
        scorenumlbl.config(text=score)
        check.config(text="\n\nThat is not correct")
        e1.delete(0, END)

root = Tk()
root.geometry('700x500')
root.title('Trivia')
root.configure(background='#f5f0e1')

Label(root, text='\n', bg="#f5f0e1") .pack(side=TOP) # To add a space in between
title = Label(root, font=('ms serif', 50, 'bold'), text='✎ TRIVIA', fg='#ff6e40', bg='#f5f0e1')
title.pack(side=TOP)

Label(root, text='\n', bg="#f5f0e1") .pack(side=TOP) # To add a space in between

question_frame = Frame(root)
question_frame.pack(side=TOP)
instructions_label = Label(question_frame, text='Question:', bg='#f5f0e1', fg='#1e3d59', font=('ms serif', 18, 'bold'))
instructions_label.pack(side=LEFT)
lbl = Label(question_frame, font=("ms serif", 18, 'bold'), bg='#f5f0e1', fg='#ffc13b')
lbl.pack(side=LEFT)

ans1 = StringVar()
e1 = Entry(root, font = ("ms serif", 16, 'bold'), textvariable=ans1, fg='#1e3d59', bg='#f5f0e1')
e1.pack()

buttons_frame = Frame(root)
buttons_frame.pack(side=TOP)
btncheck = Button(buttons_frame, text = "Check", font = ("ms serif", 16), width=8, fg='#ffc13b',
                  relief=GROOVE, command=checkans)
btncheck.pack(side=LEFT)

btnreset = Button(buttons_frame, text="Skip", font=("ms serif", 16), width=8, fg="#ff6e40", relief=GROOVE, command=res)
btnreset.pack(side=LEFT)

check = Label(root, font=("ms serif", 18, 'bold'), bg='#f5f0e1', fg='#ff6e40')
check.pack(side=TOP)

scoreframe = Frame(root)
scoreframe.pack(side=TOP)
scorelbl = Label(scoreframe, font=('ms serif', 18, 'bold'), bg='#f5f0e1', fg='#ffc13b', text='Correct Answer Streak:')
scorelbl.pack(side=LEFT)
scorenumlbl = Label(scoreframe, font=('ms serif', 18, 'bold'), bg='#f5f0e1', fg='#1e3d59', text=score)
scorenumlbl.pack(side=LEFT)

default()
root.mainloop()
