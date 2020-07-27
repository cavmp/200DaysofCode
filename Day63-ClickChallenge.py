from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('Click Challenge')
root.geometry('500x500')
clicks = 0

def addclick():
  global clicks
  clicks = clicks + 1
  lbl.configure(text=clicks)

def step():
    for i in range(61):
        progress_bar['value'] += 1.66666667 # 100 divided by 60 (this will make a minute)
        root.update()
        time.sleep(1)
    # When time is up
    global clicks
    text = "Time's Up! \n You got {0} clicks".format(clicks)
    btn.destroy()
    start.destroy()
    lbl.config(text=text, font='Arial 50 bold')

# Progress bar timer
progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
progress_bar.pack(pady=20)

start = Button(root, text='Start', command=step)
start.pack(pady=20)

# Display clicks
lbl = Label(root, font=('Arial 225 bold'), fg='#283655', text=clicks)
lbl.pack()

btn = Button(root, text="Click me", command=addclick)
btn.pack()

root.mainloop()
