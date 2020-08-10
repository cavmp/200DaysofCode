from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk

root = Tk()
root.title('Talking Dude')

canvas = Canvas(root, width=500, height=500, bg="white")
canvas.grid(row=0, column=0, columnspan=2)

bubbles = []

class BotBubble:
    def __init__(self,master,message=""):
        self.master = master
        self.frame = Frame(master,bg="light grey")
        self.i = self.master.create_window(350,100,window=self.frame)
        Label(self.frame,text=datetime.now().strftime("%Y-%m-%d %H:%m"),font=("Helvetica", 7),bg="light grey").grid(row=0,column=0,sticky="w",padx=5)
        Label(self.frame, text=message,font=("Helvetica", 15),bg="light grey").grid(row=1, column=0,sticky="w",padx=5)
        root.update_idletasks()
        self.master.create_polygon(self.draw_triangle(self.i), fill="light grey", outline="light grey")

    def draw_triangle(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2

def send_message():
    if bubbles:
        canvas.move(ALL, 0, -65)
    a = BotBubble(canvas,message=entry.get())
    bubbles.append(a)

entry = Entry(root,width=26)
entry.grid(row=1,column=0)
Button(root,text="Send",command=send_message).grid(row=1,column=1)

talking_dude = Image.open('images/talkingdude.png')
talking_dude = talking_dude.resize((220, 190), Image.ANTIALIAS) # Resize the image
talking_dude = ImageTk.PhotoImage(talking_dude)

dude = Label(root, image=talking_dude)
dude.grid(row=0, column=0)

root.mainloop()
