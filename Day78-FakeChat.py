from tkinter import *
from datetime import datetime

root = Tk()
root.title('Text Message')

canvas = Canvas(root, width=500, height=500, bg="white")
canvas.grid(row=0, column=0, columnspan=3)

bubbles = []

class SenderBotBubble:
    def __init__(self,master,message=""):
        self.master = master
        self.frame = Frame(master,bg="#4dbae6")
        self.i = self.master.create_window(450,450,window=self.frame)
        Label(self.frame,text=datetime.now().strftime("%Y-%m-%d %H:%m"),font=("Helvetica", 7),bg="#4dbae6").grid(row=0,column=0,sticky="w",padx=5)
        Label(self.frame, text=message,font=("Helvetica", 10),bg="#4dbae6").grid(row=1, column=0,sticky="w",padx=5)
        root.update_idletasks()
        self.master.create_polygon(self.draw_triangle(self.i), fill="#4dbae6", outline="#4dbae6")

    def draw_triangle(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2

class ReceiverBotBubble:
    def __init__(self,master,message=""):
        self.master = master
        self.frame = Frame(master,bg="lightgrey")
        self.i = self.master.create_window(80,450,window=self.frame)
        Label(self.frame,text=datetime.now().strftime("%Y-%m-%d %H:%m"),font=("Helvetica", 7),bg="lightgrey").grid(row=0,column=0,sticky="w",padx=5)
        Label(self.frame, text=message,font=("Helvetica", 10),bg="lightgrey").grid(row=1, column=0,sticky="w",padx=5)
        root.update_idletasks()
        self.master.create_polygon(self.draw_triangle(self.i), fill="lightgrey", outline="lightgrey")

    def draw_triangle(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x2, y2 - 10, x2 + 15, y2 + 10, x2, y2

def send_message():
    if bubbles:
        canvas.move(ALL, 0, -65)
    a = SenderBotBubble(canvas,message=send_entry.get())
    bubbles.append(a)

def receive_message():
    if bubbles:
        canvas.move(ALL, 0, -65)
    b = ReceiverBotBubble(canvas, message=receive_entry.get())
    bubbles.append(b)

receive_entry = Entry(root,width=26)
receive_entry.grid(row=1,column=0)
Button(root,text="Send",command=receive_message).grid(row=1,column=1)
send_entry = Entry(root,width=26)
send_entry.grid(row=1,column=2)
Button(root,text="Send",command=send_message).grid(row=1,column=3)

root.mainloop()
