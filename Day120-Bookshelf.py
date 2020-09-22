from tkinter import *
import sqlite3

def create():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,title TEXT,author TEXT, date TEXT)")
    con.commit()
    con.close()

def viewall():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    con.close()
    return rows

def search(title="",author="",date=""):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR date=?",(title,author,date))
    rows = cur.fetchall()
    con.close()
    return rows

def add(title,author,date):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?)",(title,author,date))
    con.commit()
    con.close()

def update(id,title,author,date):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("UPDATE books SET title=?,author=?,date=? WHERE id=?",(title,author,date,id))
    con.commit()
    con.close()

def delete(id):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    con.commit()
    con.close()

create()
window = Tk()
window.title("Bookshelf")

def view_command():
    lb.delete(0,END)
    for row in viewall():
        lb.insert(END,row)

def search_command():
    lb.delete(0,END)
    for row in search(title=title.get(),author=author.get(),date=date.get()):
        lb.insert(END,row)

def add_command():
    add(title.get(),author.get(),date.get())
    lb.delete(0,END)
    lb.insert(END,title.get(),author.get(),date.get())

def get_selected_row(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
    except IndexError:
        pass

def update_command():
    update(selected_tuple[0],title.get(),author.get(),date.get())
    view_command()

def delete_command():
    delete(selected_tuple[0])
    view_command()

def clear_command():
    lb.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

l1 = Label(window,text="Title")
l1.grid(row=0,column=0,columnspan=2)
l2 = Label(window,text="Author")
l2.grid(row=1,column=0,columnspan=2)
l3 = Label(window,text="Date Finished")
l3.grid(row=2,column=0,columnspan=2)

title=StringVar()
e1 = Entry(window,textvariable=title,width=50)
e1.grid(row=0,column=0,columnspan=10)

author=StringVar()
e2 = Entry(window,textvariable=author,width=50)
e2.grid(row=1,column=0,columnspan=10)

date=StringVar()
e3 = Entry(window,textvariable=date,width=50)
e3.grid(row=2,column=0,columnspan=10)

b1 = Button(window,text="Add",width=12,command=add_command)
b1.grid(row=5,column=0)

b2 = Button(window,text="Update",width=12,command=update_command)
b2.grid(row=5,column=1)

b3 = Button(window,text="Search",width=12,command=search_command)
b3.grid(row=5,column=2)

b4 = Button(window,text="View All",width=12,command=view_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=5,column=4)

b6 = Button(window,text="Exit",width=12,command=window.destroy)
b6.grid(row=5,column=5)

b7 = Button(window,text="Clear All",width=12,command=clear_command)
b7.grid(row=0,column=5)

lb=Listbox(window,height=20,width=94)
lb.grid(row=6,column=0,columnspan=6)

sb=Scrollbar(window)
sb.grid(row=6,column=6,rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()
