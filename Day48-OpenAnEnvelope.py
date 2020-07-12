from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('900x700')
root.title('Open an Envelope')

Label(root, text='\n') .pack(side=TOP) # To add a space in between
title = Label(root, font=('ms serif', 50, 'bold'), text='♡♡ OPEN AN ENVELOPE ♡♡', fg='#264d59')
title.pack(side=TOP)

top_frame = Frame(root)
top_frame.pack(side=TOP)
bottom_frame = Frame(root)
bottom_frame.pack(side=TOP)

def blue_env_letter():
    top = Toplevel()
    top.title('Letter')
    top.configure(background='#264d59')
    message = Label(top, font=('ms serif', 30, 'bold', 'italic'), fg='#43978d', bg='#f9ad6a',
                    text="\n\nTo whoever is reading this,\n"
                               "\nI want you to know that you aren't alone. You not only "
                               "\nhave great people by your side, but you are always in"
                               "\nGod's grace. If you really feel alone, don't fret. Something"
                                "\nor someone great is coming you way; heck, that person"
                               "\nmight already be in your life! He or she will turn your"
                               "\nlife around for the better, and will help you realize the"
                               "\nbeauty in the little things in life."
                                "\n\n ♡♡♡♡\n\n")
    message.pack(side=TOP)

blue_env_pic = Image.open('images/blue_env.jpg')
blue_env_pic = blue_env_pic.resize((300, 300), Image.ANTIALIAS) # Resize the image
blue_env_pic = ImageTk.PhotoImage(blue_env_pic)
blue_env = Button(top_frame, image=blue_env_pic, command=blue_env_letter)
blue_env.pack(side=LEFT)

def darkpink_env_letter():
    top = Toplevel()
    top.title('Letter')
    top.configure(background='#43978d')
    message = Label(top, font=('ms serif', 30, 'bold', 'italic'), fg='#264d59', bg='#43978d',
                    text="\n\nTo whoever is reading this,\n"
                               "\nI know you have been working tirelessly to achieve what"
                                "\nyou set out to do. Know that I believe in you! The tasks"
                                "\nmay be so daunting, but know that I am here to cheer you"
                                "\non! I am already so proud of what you've been able to"
                                "\nachieve. Don't give up, and never stop giving it your all!"
                                "\n\n ♡♡♡♡\n\n")
    message.pack(side=TOP)

darkpink_env_pic = Image.open('images/darkpink_env.jpg')
darkpink_env_pic = darkpink_env_pic.resize((305, 305), Image.ANTIALIAS) # Resize the image
darkpink_env_pic = ImageTk.PhotoImage(darkpink_env_pic)
darkpink_env = Button(top_frame, image=darkpink_env_pic, command=darkpink_env_letter)
darkpink_env.pack(side=LEFT)

def lightblue_env_letter():
    top = Toplevel()
    top.title('Letter')
    top.configure(background='#264d59')
    message = Label(top, font=('ms serif', 30, 'bold', 'italic'), fg='#f9ad6a', bg='#264d59',
                    text="\n\nTo whoever is reading this,\n"
                               "\nif you have recently fallen for someone beautiful, please"
                                "\ndon't get attached. I am not saying he or she isn't the"
                                "\none, but you may end up getting hurt, which is something"
                                "\nyou don't deserve! The man or woman of your dreams will"
                                "\ntreat you well, and know that he/she is out there waiting"
                                "\nfor you too!"
                                "\n\n ♡♡♡♡\n\n")
    message.pack(side=TOP)

lightblue_env_pic = Image.open('images/lightblue_env.jpg')
lightblue_env_pic = lightblue_env_pic.resize((285, 285), Image.ANTIALIAS) # Resize the image
lightblue_env_pic = ImageTk.PhotoImage(lightblue_env_pic)
lightblue_env = Button(top_frame, image=lightblue_env_pic, command=lightblue_env_letter)
lightblue_env.pack(side=LEFT)

def pink_env_letter():
    top = Toplevel()
    top.title('Letter')
    top.configure(background='#d46c4e')
    message = Label(top, font=('ms serif', 30, 'bold', 'italic'), fg='#f9e07f', bg='#d46c4e',
                    text="\n\nTo whoever is reading this,\n"
                               "\n I hope that you are able to realize the beauty in yourself!"
                                "\nKnow that while you may appreciate others, and praise them"
                                "\nfor whatever they may have or may have done, know that you"
                                "\nare even more deserving of that praise! While it may be"
                                "\nhard, focus on yourself every now and then and you will"
                                "\nstart to reap the rewards of self love!"
                                "\n\n ♡♡♡♡\n\n")
    message.pack(side=TOP)

pink_env_pic = Image.open('images/pink_env.jpg')
pink_env_pic = pink_env_pic.resize((300, 300), Image.ANTIALIAS)
pink_env_pic = ImageTk.PhotoImage(pink_env_pic)
pink_env = Button(bottom_frame, image=pink_env_pic, command=pink_env_letter)
pink_env.pack(side=LEFT)

def white_env_letter():
    top = Toplevel()
    top.title('Letter')
    top.configure(background='#f9e07f')
    message = Label(top, font=('ms serif', 30, 'bold', 'italic'), fg='#d46c4e', bg='#f9e07f',
                    text="\n\nTo whoever is reading this,\n"
                               "\n I hope that you are able to realize the beauty in yourself!"
                                "\nKnow that while you may appreciate others, and praise them"
                                "\nfor whatever they may have or may have done, know that you"
                                "\nare even more deserving of that praise! While it may be"
                                "\nhard, focus on yourself every now and then and you will"
                                "\nstart to reap the rewards of self love!"
                                "\n\n ♡♡♡♡\n\n")
    message.pack(side=TOP)

white_env_pic = Image.open('images/white_env.jpg')
white_env_pic = white_env_pic.resize((360, 360), Image.ANTIALIAS)
white_env_pic = ImageTk.PhotoImage(white_env_pic)
white_env = Button(bottom_frame, image=white_env_pic, command=white_env_letter)
white_env.pack(side=LEFT)

root.mainloop()
