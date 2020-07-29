import socket
from tkinter import *

root = Tk()
root.title("What's my IP Address?")
root.geometry('800x600')

label1 = Label(root, text='\n\n\n\n\nYour IP Address is:', font=('times new roman', 35))
label1.pack(anchor=CENTER)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

label2 = Label(root, text=ip_address, font=('times new roman', 70, 'bold'))
label2.pack(anchor=CENTER)

root.mainloop()
