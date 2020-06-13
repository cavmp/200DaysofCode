from tkinter import *
import time

def tick():
    time_string = time.strftime("%H:%M:%S") # Time module to get current local time of the user's device
    clock.config(text=time_string) # Tells the program that if the time and string has changed, the time will be updated
    clock.after(200, tick)

root = Tk() # Pop up window for the clock
root.title('Digital Clock') # Title of the window
clock = Label(root, font=("times", 150, "bold"), bg="white")
clock.grid(row=0, column=1) # Position of the clock
tick()
root.mainloop()
