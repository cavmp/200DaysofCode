from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('900x700')
root.title('Open a Door')

Label(root, text='\n') .pack(side=TOP) # To add a space in between
title = Label(root, font=('arial', 70, 'bold'), text='OPEN A DOOR', fg='#50514f')
title.pack(side=TOP)

instructions = Label(root, font=('arial', 20), text="\nThere are three doors. \n "
                                                    "Behind two doors there are scary things. \n"
                                                    "Behind one door is a good thing.\n"
                                                   "Choose a door...\n")
instructions.pack(side=TOP)

top_frame = Frame(root)
top_frame.pack(side=TOP)

def blue():
    image = (Image.open('images/scary1.jpg'))
    image.show()

blue_door_pic = Image.open('images/blue_door.png')
blue_door_pic = ImageTk.PhotoImage(blue_door_pic)
blue_door = Button(top_frame, image=blue_door_pic, command=blue)
blue_door.pack(side=LEFT)

def green():
    image = (Image.open('images/cute.jpg'))
    image.show()

green_door_pic = Image.open('images/green_door.png')
green_door_pic = ImageTk.PhotoImage(green_door_pic)
green_door = Button(top_frame, image=green_door_pic, command=green)
green_door.pack(side=LEFT)

def orange():
    image = (Image.open('images/scary2.png'))
    image.show()

orange_door_pic = Image.open('images/orange_door.png')
orange_door_pic = ImageTk.PhotoImage(orange_door_pic)
orange_door = Button(top_frame, image=orange_door_pic, command=orange)
orange_door.pack(side=LEFT)


root.mainloop()
