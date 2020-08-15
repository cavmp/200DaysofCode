from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('600x700')
root.title('Mad Libs Game')

title = Label(root, text='Mad Libs Game', font=('Courier', 40, 'bold')) .pack(pady=40)
instruction = Label(root, text='Select a Category', font=('Courier', 20, 'bold')) .pack(side=TOP)

# Frame for the options
top_frame = Frame(root)
top_frame.pack(pady=20)

bottom_frame = Frame(root)
bottom_frame.pack(pady=20)

# Commands for options
def vacation_madlib():
    top = Toplevel()
    top.title('Mad Libs Game: VACATION')
    top.geometry('600x700')

    vacation_title = Label(top, text='Mad Libs: Vacation ☀', font=('Courier', 40, 'bold')).pack(pady=40)

    # First line
    frame1 = Frame(top)
    frame1.pack(side=TOP)
    Label(frame1, text='A vacation is when you take a trip to some') .pack(side=LEFT)
    entry1 = Entry(frame1, width=10)
    entry1.pack(side=LEFT)
    entry1.insert(0, '(adjective)')
    Label(frame1, text='place with your') .pack(side=LEFT)

    # Second line
    frame2 = Frame(top)
    frame2.pack(side=TOP)
    entry2 = Entry(frame2, width=10)
    entry2.pack(side=LEFT)
    entry2.insert(0, '(adjective)')
    Label(frame2, text='family. Usually you go to some place that is near a/an') .pack(side=LEFT)

    # Third line
    frame3 = Frame(top)
    frame3.pack(side=TOP)
    entry3 = Entry(frame3, width=10)
    entry3.pack(side=LEFT)
    entry3.insert(0, '(noun)')
    Label(frame3, text='or up a/an') .pack(side=LEFT)
    entry4 = Entry(frame3, width=10)
    entry4.pack(side=LEFT)
    entry4.insert(0, '(noun)')
    Label(frame3, text='. A good vacation place is one where') .pack(side=LEFT)

    # Fourth line
    frame4 = Frame(top)
    frame4.pack(side=TOP)
    Label(frame4, text='you can ride') .pack(side=LEFT)
    entry5 = Entry(frame4, width=10)
    entry5.pack(side=LEFT)
    entry5.insert(0, '(plural noun)')
    Label(frame4, text='. I like to spend my time') .pack(side=LEFT)
    entry6 = Entry(frame4, width=10)
    entry6.pack(side=LEFT)
    entry6.insert(0, '(verb ending in "ing")')
    Label(frame4, text='or') .pack(side=LEFT)

    # Fifth line
    frame5 = Frame(top)
    frame5.pack(side=TOP)
    entry7 = Entry(frame5, width=10)
    entry7.pack(side=LEFT)
    entry7.insert(0, '(verb ending in "ing")')
    Label(frame5, text='. When parents go on a vacation, they spend their time') .pack(side=LEFT)

    # Sixth line
    frame6 = Frame(top)
    frame6.pack(side=TOP)
    Label(frame6, text='eating three') .pack(side=LEFT)
    entry7 = Entry(frame6, width=10)
    entry7.pack(side=LEFT)
    entry7.insert(0, '(plural noun)')
    Label(frame6, text='a day, and fathers play golf, and mothers sit around') .pack(side=LEFT)

    # Seventh line
    frame7 = Frame(top)
    frame7.pack(side=TOP)
    entry8 = Entry(frame7, width=10)
    entry8.pack(side=LEFT)
    entry8.insert(0, '(verb ending in "ing")')
    Label(frame7, text='. Last summer, my little brother fell in a/an') .pack(side=LEFT)
    entry9 = Entry(frame7, width=10)
    entry9.pack(side=LEFT)
    entry9.insert(0, '(noun)')
    Label(frame7, text='and got') .pack(side=LEFT)

    # 8th line
    frame8 = Frame(top)
    frame8.pack(side=TOP)
    Label(frame8, text='poison') .pack(side=LEFT)
    entry10 = Entry(frame8, width=10)
    entry10.pack(side=LEFT)
    entry10.insert(0, '(plant)')
    Label(frame8, text='all over his') .pack(side=LEFT)
    entry11 = Entry(frame8, width=10)
    entry11.pack(side=LEFT)
    entry11.insert(0, '(part of body)')
    Label(frame8, text='. My family is going to go') .pack(side=LEFT)

    # Ninth line
    frame9 = Frame(top)
    frame9.pack(side=TOP)
    Label(frame9, text='to (the)') .pack(side=LEFT)
    entry12 = Entry(frame9, width=10)
    entry12.pack(side=LEFT)
    entry12.insert(0, '(a place)')
    Label(frame9, text=', and I will practice') .pack(side=LEFT)
    entry13 = Entry(frame9, width=10)
    entry13.pack(side=LEFT)
    entry13.insert(0, '(verb ending in "ing")')
    Label(frame9, text='. Parents need') .pack(side=LEFT)

    # Tenth line
    frame10 = Frame(top)
    frame10.pack(side=TOP)
    Label(frame10, text='vacations more than kids because parents are always very') .pack(side=LEFT)
    entry14 = Entry(frame10, width=10)
    entry14.pack(side=LEFT)
    entry14.insert(0, '(adjective)')

    # Eleventh line
    frame11 = Frame(top)
    frame11.pack(side=TOP)
    Label(frame11, text='and because they have to work') .pack(side=LEFT)
    entry14 = Entry(frame11, width=10)
    entry14.pack(side=LEFT)
    entry14.insert(0, '(number)')
    Label(frame11, text='hours every day all year making') .pack(side=LEFT)

    # Twelfth line
    frame12 = Frame(top)
    frame12.pack(side=TOP)
    Label(frame12, text='enough') .pack(side=LEFT)
    entry15 = Entry(frame12, width=10)
    entry15.pack(side=LEFT)
    entry15.insert(0, '(plural noun)')
    Label(frame12, text='to pay for the vacation.') .pack(side=LEFT)

    # Source
    Label(top, text='From https://www.madlibs.com/wp-content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf'
                    '\n Copyright © 1988 by Price Stern Sloan, a division of Penguin Putnam Books for Young Readers, '
                    'New York.', font=('Arial', 10)) .pack(side=BOTTOM, pady=30)

def invitation_madlib():
    top = Toplevel()
    top.title('Mad Libs Game: PARTY INVITATION')
    top.geometry('600x700')

    invitation_title = Label(top, text='​🎉Mad Libs: Party Invitation', font=('Courier', 30, 'bold')).pack(pady=40)

    # First line
    frame1 = Frame(top)
    frame1.pack(side=TOP)
    entry1 = Entry(frame1, width=10, font=('Arial', 20))
    entry1.pack(side=LEFT)
    entry1.insert(0, '(name)')
    Label(frame1, text='is having a', font=('Arial', 20)).pack(side=LEFT)
    entry2 = Entry(frame1, width=10, font=('Arial', 20))
    entry2.pack(side=LEFT)
    entry2.insert(0, '(theme)')
    Label(frame1, text='party!', font=('Arial', 20)).pack(side=LEFT)

    # Second line
    frame2 = Frame(top)
    frame2.pack(side=TOP)
    Label(frame2, text="It's going to be at", font=('Arial', 20)).pack(side=LEFT)
    entry3 = Entry(frame2, width=10, font=('Arial', 20))
    entry3.pack(side=LEFT)
    entry3.insert(0, '(a place)')
    Label(frame2, text="on", font=('Arial', 20)).pack(side=LEFT)
    entry4 = Entry(frame2, width=10, font=('Arial', 20))
    entry4.pack(side=LEFT)
    entry4.insert(0, '(day of the week)')
    Label(frame2, text=".", font=('Arial', 20)).pack(side=LEFT)

    # Third line
    frame3 = Frame(top)
    frame3.pack(side=TOP)
    Label(frame3, text="Please make sure to show up at", font=('Arial', 20)).pack(side=LEFT)
    entry5 = Entry(frame3, width=10, font=('Arial', 20))
    entry5.pack(side=LEFT)
    entry5.insert(0, '(time)')
    Label(frame3, text=", or else", font=('Arial', 20)).pack(side=LEFT)

    # Fourth line
    frame4 = Frame(top)
    frame4.pack(side=TOP)
    Label(frame4, text="you will be required to", font=('Arial', 20)).pack(side=LEFT)
    entry6 = Entry(frame4, width=10, font=('Arial', 20))
    entry6.pack(side=LEFT)
    entry6.insert(0, '(verb)')
    Label(frame4, text="a/an", font=('Arial', 20)).pack(side=LEFT)
    entry7 = Entry(frame4, width=10, font=('Arial', 20))
    entry7.pack(side=LEFT)
    entry7.insert(0, '(animal)')

    # Fifth line
    frame5 = Frame(top)
    frame5.pack(side=TOP)
    Label(frame5, text="with your", font=('Arial', 20)).pack(side=LEFT)
    entry8 = Entry(frame5, width=10, font=('Arial', 20))
    entry8.pack(side=LEFT)
    entry8.insert(0, '(body part)')
    Label(frame5, text=".", font=('Arial', 20)).pack(side=LEFT)

    frame6 = Frame(top)
    frame6.pack(pady=20)
    Label(frame6, text="RSVP at", font=('Arial', 20)).pack(side=LEFT)
    entry9 = Entry(frame6, width=10, font=('Arial', 20))
    entry9.pack(side=LEFT)
    entry9.insert(0, '(contact information)')

    # Source
    Label(top, text='From https://www.madlibs.com/wp-content/uploads/2016/04/KIDS-invitation_1_.pdf',
                    font=('Arial', 10)).pack(side=BOTTOM, pady=30)

def valentine_madlib():
    top = Toplevel()
    top.title("Mad Libs Game: VALENTINE'S DAY CARD")
    top.geometry('600x700')

    valentine_title = Label(top, text="♥Mad Libs: Valentine's Day Card♥", font=('Courier', 30, 'bold')).pack(pady=40)

    # First line
    frame1 = Frame(top)
    frame1.pack(side=TOP)
    Label(frame1, text='Dear', font=('Times', 20)).pack(side=LEFT)
    entry1 = Entry(frame1, width=15, font=('times', 20))
    entry1.pack(side=LEFT)
    entry1.insert(0, '(name of person)')
    Label(frame1, text=',', font=('times', 20)).pack(side=LEFT)

    # Second line
    frame2 = Frame(top)
    frame2.pack(side=TOP)
    entry2 = Entry(frame2, width=15, font=('times', 20))
    entry2.pack(side=LEFT)
    entry2.insert(0, '(plural noun)')
    Label(frame2, text='are red,', font=('times', 20)).pack(side=LEFT)

    # Third line
    frame3 = Frame(top)
    frame3.pack(side=TOP)
    entry3 = Entry(frame3, width=15, font=('times', 20))
    entry3.pack(side=LEFT)
    entry3.insert(0, '(plural noun)')
    Label(frame3, text='are blue,', font=('times', 20)).pack(side=LEFT)

    # Fourth line
    frame4 = Frame(top)
    frame4.pack(side=TOP)
    Label(frame4, text='You love me and', font=('times', 20)).pack(side=LEFT)

    # Fifth line
    frame5 = Frame(top)
    frame5.pack(side=TOP)
    Label(frame5, text='I love', font=('times', 20)).pack(side=LEFT)
    entry4 = Entry(frame5, width=15, font=('times', 20))
    entry4.pack(side=LEFT)
    entry4.insert(0, '(plural noun)')
    Label(frame5, text='!', font=('times', 20)).pack(side=LEFT)

    # Sixth line
    frame6 = Frame(top)
    frame6.pack(pady=30)
    Label(frame6, text='From', font=('times', 20)).pack(side=LEFT)
    entry4 = Entry(frame6, width=15, font=('times', 20))
    entry4.pack(side=LEFT)
    entry4.insert(0, '(name)')

    # Source
    Label(top, text='From https://www.madlibs.com/wp-content/uploads/2016/04/ValentinesDayCard2-flat.pdf',
          font=('Arial', 10)).pack(side=BOTTOM, pady=30)

def hallpass_madlib():
    top = Toplevel()
    top.title("Mad Libs Game: HALL PASS")
    top.geometry('600x700')

    hallpass_title = Label(top, text="Mad Libs: Hall Pass", font=('Courier', 30, 'bold')).pack(pady=40)

    # First line
    frame1 = Frame(top)
    frame1.pack(side=TOP)
    Label(frame1, text='DATE:', font=('Courier', 20)).pack(side=LEFT)
    entry1 = Entry(frame1, width=15, font=('Courier', 20))
    entry1.pack(side=LEFT)

    # Second line
    frame2 = Frame(top)
    frame2.pack(pady=20)
    entry2 = Entry(frame2, width=15, font=('courier', 20))
    entry2.pack(side=LEFT)
    entry2.insert(0, '(name)')
    Label(frame2, text='is authorized', font=('Courier', 20)).pack(side=LEFT)

    # Third line
    frame3 = Frame(top)
    frame3.pack(side=TOP)
    Label(frame3, text='to be at', font=('Courier', 20)).pack(side=LEFT)
    entry3 = Entry(frame3, width=15, font=('courier', 20))
    entry3.pack(side=LEFT)
    entry3.insert(0, '(a place)')

    # Fourth line
    frame4 = Frame(top)
    frame4.pack(side=TOP)
    Label(frame4, text='instead of', font=('Courier', 20)).pack(side=LEFT)
    entry4 = Entry(frame4, width=15, font=('courier', 20))
    entry4.pack(side=LEFT)
    entry4.insert(0, '(noun)')
    Label(frame4, text='class', font=('Courier', 20)).pack(side=LEFT)

    # Fifth line
    frame5 = Frame(top)
    frame5.pack(pady=50)
    Label(frame5, text='Signed:', font=('Courier', 20)).pack(side=LEFT)
    entry5 = Entry(frame5, width=15, font=('Courier', 20))
    entry5.pack(side=LEFT)

    # Source
    Label(top, text='From https://www.madlibs.com/wp-content/uploads/2016/04/KIDS-excuse-hall-pass_1_.pdf',
          font=('Arial', 10)).pack(side=BOTTOM, pady=30)

# Options
vacation_img = Image.open('images/vacation.png')
vacation_img = vacation_img.resize((200, 200), Image.ANTIALIAS)
vacation_img = ImageTk.PhotoImage(vacation_img)
vacation = Button(top_frame, image=vacation_img, command=vacation_madlib)
vacation.pack(side=LEFT)

invitation_img = Image.open('images/invitation.jpg')
invitation_img = invitation_img.resize((200, 200), Image.ANTIALIAS)
invitation_img = ImageTk.PhotoImage(invitation_img)
invitation = Button(top_frame, image=invitation_img, command=invitation_madlib)
invitation.pack(side=LEFT)

valentine_img = Image.open('images/valentine.jpg')
valentine_img = valentine_img.resize((200, 200), Image.ANTIALIAS)
valentine_img = ImageTk.PhotoImage(valentine_img)
valentine = Button(bottom_frame, image=valentine_img, command=valentine_madlib)
valentine.pack(side=LEFT)

hallpass_img = Image.open('images/hallpass.png')
hallpass_img = hallpass_img.resize((200, 200), Image.ANTIALIAS)
hallpass_img = ImageTk.PhotoImage(hallpass_img)
hallpass = Button(bottom_frame, image=hallpass_img, command=hallpass_madlib)
hallpass.pack(side=LEFT)

root.mainloop()
