from tkinter import *

root = Tk()
root.geometry('600x750')
root.title('How Eco-Friendly Are You?')

eco_score = 0

Label(root, text='How eco-friendly are you?', font=('ms serif', 40, 'bold'), fg='#326229') .pack(pady=20)

frame = Frame(root)
frame.pack(pady=10)
Label(frame, text='Eco Score: ', font=('ms serif', 15, 'bold')) .pack(side=LEFT)
score = Label(frame)
score.pack(side=LEFT)

def minus_100():
    global eco_score
    eco_score -= 100
    score.configure(text=eco_score)

def minus_50():
    global eco_score
    eco_score -= 50
    score.configure(text=eco_score)

def minus_30():
    global eco_score
    eco_score -= 30
    score.configure(text=eco_score)

def minus_25():
    global eco_score
    eco_score -= 25
    score.configure(text=eco_score)

def minus_20():
    global eco_score
    eco_score -= 20
    score.configure(text=eco_score)

def minus_10():
    global eco_score
    eco_score -= 10
    score.configure(text=eco_score)

def plus_10():
    global eco_score
    eco_score += 10
    score.configure(text=eco_score)

def plus_20():
    global eco_score
    eco_score += 20
    score.configure(text=eco_score)

def plus_30():
    global eco_score
    eco_score += 30
    score.configure(text=eco_score)

def plus_50():
    global eco_score
    eco_score += 50
    score.configure(text=eco_score)

def plus_100():
    global eco_score
    eco_score += 100
    score.configure(text=eco_score)

Label(root, text='1) How do you come to school/ work?', font=('ms serif', 15), fg='#06283b') .pack(pady=10)
frame1 = Frame(root) # Frame for the buttons
frame1.pack(side=TOP)
Button(frame1, text='By Car', command=minus_50) .pack(side=LEFT)
Button(frame1, text='By Bus', command=minus_10) .pack(side=LEFT)
Button(frame1, text='On Foot', command=plus_100) .pack(side=LEFT)
Button(frame1, text='On a bike/ scooter', command=plus_100) .pack(side=LEFT)

Label(root, text='2) Did you travel by plane in the last 12 months?', font=('ms serif', 15), fg='#06283b') .pack(pady=10)
frame2 = Frame(root) # Frame for the buttons
frame2.pack(side=TOP)
Button(frame2, text='No', command=plus_100) .pack(side=LEFT)
Button(frame2, text='Once', command=minus_25) .pack(side=LEFT)
Button(frame2, text='Twice', command=minus_50) .pack(side=LEFT)
Button(frame2, text='Atleast three times', command=minus_100) .pack(side=LEFT)

Label(root, text='3) Do you use your recycling bins at home?', font=('ms serif', 15), fg='#06283b') .pack(pady=10)
frame3 = Frame(root) # Frame for the buttons
frame3.pack(side=TOP)
Button(frame3, text='Never', command=minus_50) .pack(side=LEFT)
Button(frame3, text='Rarely', command=plus_10) .pack(side=LEFT)
Button(frame3, text='Often', command=plus_50) .pack(side=LEFT)
Button(frame3, text='Regularly', command=plus_100) .pack(side=LEFT)

Label(root, text='4) When you go shopping do you?', font=('ms serif', 15), fg='#06283b') .pack(pady=10)
frame3 = Frame(root) # Frame for the buttons
frame3.pack(side=TOP)
Button(frame3, text='Bring your own reusable carrier bags', command=plus_20) .pack(side=LEFT)
Button(frame3, text='Ask for plastic bags', command=minus_20) .pack(side=LEFT)

Label(root, text='5) At home do you use Energy saving bulbs?', font=('ms serif', 15), fg='#06283b') .pack(pady=10)
frame3 = Frame(root) # Frame for the buttons
frame3.pack(side=TOP)
Button(frame3, text='Yes', command=plus_30) .pack(side=LEFT)
Button(frame3, text='No', command=minus_30) .pack(side=LEFT)

Label(root, text='6) When you clean your teeth, do you let the water run?', font=('ms serif', 15), fg='#06283b') .pack(pady=10)
frame3 = Frame(root) # Frame for the buttons
frame3.pack(side=TOP)
Button(frame3, text='Yes', command=minus_30) .pack(side=LEFT)
Button(frame3, text='Sometimes', command=minus_10) .pack(side=LEFT)
Button(frame3, text='Never', command=plus_20) .pack(side=LEFT)

Label(root, text='7) Is your house equipped with solar panels?', font=('ms serif', 15), fg='#06283b') .pack(pady=10)
frame3 = Frame(root) # Frame for the buttons
frame3.pack(side=TOP)
Button(frame3, text='Yes', command=minus_30) .pack(side=LEFT)
Button(frame3, text='No') .pack(side=LEFT)

Label(root, text='8) When it’s getting a bit colder at the end of the summer do you?', font=('ms serif', 15), fg='#06283b') .pack(pady=10)
frame3 = Frame(root) # Frame for the buttons
frame3.pack(side=TOP)
Button(frame3, text='Put an extra layer on (e.g. jumper, extra blanket)', command=plus_50) .pack(side=LEFT)
Button(frame3, text='Turn the heater on', command=minus_50) .pack(side=LEFT)

root.mainloop()
