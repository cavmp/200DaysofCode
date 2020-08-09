from tkinter import *
import random
import webbrowser
from PIL import Image, ImageTk

songs = ['https://www.youtube.com/watch?v=bc0KhhjJP98', 'https://www.youtube.com/watch?v=jzXt7YvK9Hw',
         'https://www.youtube.com/watch?v=4iB8VUSMfjE', 'https://www.youtube.com/watch?v=SQdgdWayPhQ',
         'https://www.youtube.com/watch?v=9zEl-FQLI4A', 'https://www.youtube.com/watch?v=ox7RsX1Ee34',
         'https://www.youtube.com/watch?v=6nhqnJKOvZ8', 'https://www.youtube.com/watch?v=HqYAgDYvdDw',
         'https://www.youtube.com/watch?v=EgBJmlPo8Xw', 'https://www.youtube.com/watch?v=sZd-t5-I5uA',
         'https://www.youtube.com/watch?v=wXhTHyIgQ_U', 'https://www.youtube.com/watch?v=_83KqwEEGw4',
         'https://www.youtube.com/watch?v=XpqqjU7u5Yc', 'https://www.youtube.com/watch?v=xrPjip1R5lo',
         'https://www.youtube.com/watch?v=ZyDcktys9EU', 'https://www.youtube.com/watch?v=Ka4BxFizU7I',
         'https://www.youtube.com/watch?v=7xzU9Qqdqww', 'https://www.youtube.com/watch?v=GBVotNefYME',
         'https://www.youtube.com/watch?v=fzzMOMkjm8A', 'https://www.youtube.com/watch?v=ApXoWvfEYVU',
         'https://www.youtube.com/watch?v=AjGkbFqi67c', 'https://www.youtube.com/watch?v=QYh6mYIJG2Y',
         'https://www.youtube.com/watch?v=r7qovpFAGrQ', 'https://www.youtube.com/watch?v=btIQvYcLNoI',
         'https://www.youtube.com/watch?v=GdJP11JwLos', 'https://www.youtube.com/watch?v=AVPEP_KSldA']

num = random.randrange(len(songs))

new = 2

def change_song():
    num = random.randrange(0, len(songs), 1)
    webbrowser.open(songs[num], new=new)

root = Tk()
root.geometry('800x500')
root.title('Get a Random Song!')


Label(root, text='\n') .pack(side=TOP) # To add a space in between
title = Label(root, font=('ms serif', 50, 'bold'), text='♫ GET A RANDOM SONG ♪', fg='#264d59')
title.pack(side=TOP)

play_button = Image.open('images/playbutton.png')
play_button = play_button.resize((150, 150), Image.ANTIALIAS) # Resize the image
play_button = ImageTk.PhotoImage(play_button)

button = Button(root, image=play_button, font=('Helvetica 20 bold'), command=change_song)
button.pack(anchor=CENTER, pady=100)

root.mainloop()
