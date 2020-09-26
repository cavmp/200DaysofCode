from tkinter import *
import sqlite3

def create():
    con = sqlite3.connect("hospital.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(id INTEGER PRIMARY KEY,name TEXT,age TEXT, gender TEXT,"
                "location TEXT,scheduled_time TEXT, phone TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("hospital.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    con.close()
    return rows

def search(name="",age="",gender="",location="", scheduled_time="", phone=""):
    con = sqlite3.connect("hospital.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE name=? OR age=? OR gender=? OR location=? OR scheduled_time=? OR phone=?",(name,age,gender,location,scheduled_time,phone))
    rows = cur.fetchall()
    con.close()
    return rows
def add(name,age,gender,location,scheduled_time,phone):
    con = sqlite3.connect("hospital.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(NULL,?,?,?,?,?,?)",(name,age,gender,location,scheduled_time,phone))
    con.commit()
    con.close()
def update(id,name,age,gender,location,scheduled_time,phone):
    con = sqlite3.connect("hospital.db")
    cur = con.cursor()
    cur.execute("UPDATE account SET name=?,age=?,gender=?,location=?,scheduled_time=?,phone=? WHERE id=?",(name,age,gender,location,scheduled_time,phone,id))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("hospital.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE id=?",(id,))
    con.commit()
    con.close()
create()
window = Tk()
window.title("Hospital Management System for Appointments")

def view_command():
    lb.delete(0,END)
    for row in viewall():
        lb.insert(END,row)

def search_command():
    lb.delete(0,END)
    for row in search(name=name.get(),age=age.get(),gender=gender.get(),location=location.get(),scheduled_time=scheduled_time.get(),phone=phone.get()):
        lb.insert(END,row)

def add_command():
    add(name.get(),age.get(),gender.get(),location.get(),scheduled_time.get(), phone.get())
    lb.delete(0,END)
    lb.insert(END,name.get(),age.get(),gender.get(),location.get(),scheduled_time.get(), phone.get())

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
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass

def update_command():
    update(selected_tuple[0],name.get(),age.get(),gender.get(),location.get(),scheduled_time.get(), phone.get())
    view_command()

def delete_command():
    delete(selected_tuple[0])
    view_command()

def clear_command():
    lb.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

l1 = Label(window,text="Name")
l1.grid(row=0,column=0,columnspan=2)
l2 = Label(window,text="Age")
l2.grid(row=1,column=0,columnspan=2)
l3 = Label(window,text="Gender")
l3.grid(row=2,column=0,columnspan=2)
l4 = Label(window,text="Location")
l4.grid(row=3,column=0,columnspan=2)
l5 = Label(window,text="Scheduled Time")
l5.grid(row=4,column=0,columnspan=2)
l5 = Label(window,text="Phone")
l5.grid(row=5,column=0,columnspan=2)

name=StringVar()
e1 = Entry(window,textvariable=name,width=50)
e1.grid(row=0,column=0,columnspan=10)

age=StringVar()
e2 = Entry(window,textvariable=age,width=50)
e2.grid(row=1,column=0,columnspan=10)

gender=StringVar()
e3 = Entry(window,textvariable=gender,width=50)
e3.grid(row=2,column=0,columnspan=10)

location=StringVar()
e4 = Entry(window,textvariable=location,width=50)
e4.grid(row=3,column=0,columnspan=10)

scheduled_time=StringVar()
e5 = Entry(window,textvariable=scheduled_time,width=50)
e5.grid(row=4,column=0,columnspan=10)

phone=StringVar()
e6 = Entry(window,textvariable=phone,width=50)
e6.grid(row=5,column=0,columnspan=10)

b1 = Button(window,text="Add Appointment",width=12,command=add_command)
b1.grid(row=6,column=0)

b2 = Button(window,text="Update",width=12,command=update_command)
b2.grid(row=6,column=1)

b3 = Button(window,text="Search",width=12,command=search_command)
b3.grid(row=6,column=2)

b4 = Button(window,text="View All",width=12,command=view_command)
b4.grid(row=6,column=3)

b5 = Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=4)

b6 = Button(window,text="Cancel",width=12,command=window.destroy)
b6.grid(row=6,column=5)

b7 = Button(window,text="Clear All",width=12,command=clear_command)
b7.grid(row=0,column=5)

lb=Listbox(window,height=20,width=94)
lb.grid(row=7,column=0,columnspan=6)

sb=Scrollbar(window)
sb.grid(row=7,column=6,rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()
