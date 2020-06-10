import tkinter as tk

HEIGHT = 250
WIDTH = 250
time = 0

def set_timer():
    global time
    time = time + int(entry.get()) # Gets the number from user's entry 
    return time

def countdown():
    global time
    if time > 0:
        label.configure(text=time)
        time = time - 1
        label.after(1000, countdown) # From the user's entry, the program will subtract one per 1000th millisecond, creating a countdown
    elif time == 0:
        print("end") # Prints 'end' in the terminal
        label.config(text="0") # Indicates that the countdown has ended


root = tk.Tk()
root.title('Countdown')
root.geometry("220x150")

label = tk.Label(root, font="times 20")
label.grid(row=1, column=2)

times = tk.StringVar()
entry = tk.Entry(root, textvariable=times)
entry.grid(row=2, column=2)

button = tk.Button(root, text='SET TIMER', width=20, command=set_timer)
button.grid(row=4, column=2, padx=20)

button2 = tk.Button(root, text='START', width=20, command=countdown)
button2.grid(row=6, column=2, padx=20)

root.mainloop()
