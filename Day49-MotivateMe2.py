from tkinter import *
from PIL import Image, ImageTk
import random

quotes = ['A little progress today adds \nup to big results', 'Your only limit is your mind',
          '“The secret of getting ahead \nis getting started.” – Mark Twain',
          '“We are what we repeatedly do. \nExcellence, then, is not an \nact, but a habit.” – Aristotle',
          '“Great things are done \nby a series of small things \nbrought together” – Vincent Van Gogh',
          '“Don’t be pushed around \nby the fears in your mind\n. Be led by the dreams \nin your heart.” – Roy T. Bennett',
          '“The only difference \nbetween ordinary and extraordinary\n is that little extra.” \n– Jimmy Johnson',
          '“If you work on something \na little bit every day, you \nend up with something that \nis massive.” – Kenneth Goldsmith',
          '“Nothing will work \nunless you do.” – Maya Angelou', 'Make each day your masterpiece. \n– John Wooden']

num = random.randrange(len(quotes))

root = Tk()
root.geometry('900x700')
root.title('Motivate Me')
root.configure(background='#a9bcd0')

Label(root, text='\n', bg='#a9bcd0') .pack(side=TOP) # To add a space in between

top_frame = Frame(root)
top_frame.pack(side=TOP)
bottom_frame = Frame(root)
bottom_frame.pack(side=TOP)

def motivate():
    global quotes, num
    top = Toplevel()
    top.geometry('700x400')
    top.title('Motivational Quote')
    top.configure(background='#58a4b0')
    lbl = Label(top, font=('ms serif', 30, 'bold', 'italic'), fg='#1b1b1e', bg='#58a4b0')
    lbl.pack(side=TOP)
    lbl.config(text=quotes[num])

motivateme_pic = Image.open('images/motivateme.jpg')
motivateme_pic = motivateme_pic.resize((350, 150), Image.ANTIALIAS) # Resize the image
motivateme_pic = ImageTk.PhotoImage(motivateme_pic)
motivateme = Button(top_frame, image=motivateme_pic, command=motivate)
motivateme.pack(side=LEFT)

def habits():
    top = Toplevel()
    top.geometry('700x400')
    top.title('Habit Websites')
    top.configure(background='#58a4b0')
    lbl = Label(top, font=('ms serif', 30, 'bold', 'italic'), fg='#1b1b1e', bg='#58a4b0', text='Visit:\n\n\nhttps://gretchenrubin.com/about/biography/'
                                                                                               '\nhttps://jamesclear.com/articles')
    lbl.pack(side=TOP)

habits_pic = Image.open('images/HABITS.jpg')
habits_pic = habits_pic.resize((300, 400), Image.ANTIALIAS) # Resize the image
habits_pic = ImageTk.PhotoImage(habits_pic)
habits = Button(bottom_frame, image=habits_pic, command=habits)
habits.pack(side=LEFT)

def book_recommend():
    top = Toplevel()
    top.geometry('700x400')
    top.title('Books')
    top.configure(background='#58a4b0')
    lbl = Label(top, font=('ms serif', 20), fg='#1b1b1e', bg='#58a4b0',
                text='Self-Help Books I recommend:\n\nSubtle Art of Not Giving a Fuck by Mark Manson\n'
                     '7 Habits of Highly Effective People by Stephen Covey\nEverything is Fucked by Mark Manson\n'
                     'Life is What You Make It by Peter Buffett\nGrit by Angela Duckworth\nThink and Grow Rich by'
                     'Napoleon Hill\nOutliers by Malcolm Gladwell\n13 Things Mentally Strong People Don’t Do\n'
                     'Atomic Habits by James Clear\nBetter than Before by Gretchen Rubin')
    lbl.pack(side=TOP)

books_pic = Image.open('images/books.jpg')
books_pic = books_pic.resize((300, 400), Image.ANTIALIAS) # Resize the image
books_pic = ImageTk.PhotoImage(books_pic)
books = Button(bottom_frame, image=books_pic, command=book_recommend)
books.pack(side=LEFT)

root.mainloop()
