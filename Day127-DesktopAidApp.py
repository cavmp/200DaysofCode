from tkinter import *
import webbrowser
from PIL import Image,ImageTk

root = Tk()
root.title("Desktop Aid App")
root.geometry("660x300")
root.resizable(False,False)

def Yt_Butt():
    string =  YtEnt.get()
    webbrowser.open("https://www.youtube.com/results?search_query="+string)
    YtEnt.delete(0,END)
def Goo_Butt():
    string = GooEnt.get()
    webbrowser.open("https://www.google.com/search?&q="+string)
    GooEnt.delete(0,END)
def Insta_Butt():
    string=InstaEnt.get()
    webbrowser.open("https://www.instagram.com/"+string)
    InstaEnt.delete(0,END)



#Youtube Section
YtEnt = Entry(root,width=45)
YtEnt.grid(row=1,column=1)
YtButt = Button(root, text="Search", command=Yt_Butt,fg="white",bg="red")
YtButt.grid(row=1,column=3)
Ytload = Image.open("images/youtube.png")
Ytload = Ytload.resize((75,75))
Ytrender = ImageTk.PhotoImage(Ytload)
Ytimg=Label(image=Ytrender)
Ytimg.grid(row=1,column=0)

#Google Section
GooEnt = Entry(root, width=45)
GooEnt.grid(row=3,column=1)
GooButt = Button(root,text="Search",command=Goo_Butt,fg="white",bg="red")
GooButt.grid(row=3,column=3)
Gooload = Image.open("images/google.png")
Gooload = Gooload.resize((75,75))
Goorender = ImageTk.PhotoImage(Gooload)
Gooimg = Label(image=Goorender)
Gooimg.grid(row=3,column=0)

#Instagram Section
InstaEnt = Entry(root, width=45)
InstaEnt.grid(row=5,column=1)
InstaButt = Button(root,text = "Go",command=Insta_Butt,fg="white",bg="red")
InstaButt.grid(row=5,column=3)
Instaload = Image.open("images/instagram.jpg")
Instaload = Instaload.resize((75,75))
Instarender = ImageTk.PhotoImage(Instaload)
Instaimg = Label(image=Instarender)
Instaimg.grid(row=5,column=0)


VerLab = Label(text="Desktop Aid", font=("arial",18)).grid(row=0,column=0)
root.mainloop()
