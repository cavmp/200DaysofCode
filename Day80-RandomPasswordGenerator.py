import random
from tkinter import *

password = []

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

def main():
    global password

    #Main program starts here
    uppercaseLetter1 = chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
    uppercaseLetter2 = chr(random.randint(65,90))
    uppercaseLetter3 = chr(random.randint(65,90))
    lowercaseLetter1 = chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
    lowercaseLetter2 = chr(random.randint(97,122))
    lowercaseLetter3 = chr(random.randint(97,122))
    digit1 = chr(random.randint(48, 57)) #Generate a random number (based on ASCII code)
    digit2 = chr(random.randint(48, 57))
    punctuationSign1 = chr(random.randint(33, 74)) #Generate a random punctuation (based on ASCII code)
    punctuationSign2 = chr(random.randint(33, 74))

    #Generate password using all the characters, in random order
    password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + lowercaseLetter1 + lowercaseLetter2 + \
           lowercaseLetter3 + digit1 + digit2 + punctuationSign1 + punctuationSign2
    password = shuffle(password)

    #Ouput
    lbl.config(text=password)
    return password

def copy_text():
    global password
    root.clipboard_clear()
    root.clipboard_append(password)

root = Tk()
root.geometry("550x320")
root.title("Random Password Generator")
root.configure(background='#eae7dc')

title = Label(root, font=('Verdana', 30, 'bold'), text='\nRandom Password Generator', bg='#eae7dc', fg='#44318d')
title.pack(side=TOP)

button = Button(root, text='GET A PASSWORD', font=('Verdana 18'), command=main)
button.pack(pady=20)

lbl = Label(root, font=("Verdana", 30), bg='#eae7dc')
lbl.pack(pady=20)

copy = Button(root, text='Copy', font=('Verdana 10'), command=copy_text)
copy.pack(pady=20)

root.mainloop()
