from tkinter import *

def click_button(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def click_clear_button():
    global operator
    operator=""
    text_input.set("")

def click_equal_button():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

root = Tk()
root.title('Calculator')
operator=""
text_input = StringVar()

user_input = Entry(root, font=('arial', 20, 'bold'), textvariable= text_input, bd=30, insertwidth=4, bg='black',
                   fg='white', justify='right') .grid(columnspan=4)

button7 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='7', bg='white', command=lambda:click_button(7)) .grid(row=1, column=0)
button8 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='8', bg='white', command=lambda:click_button(8)) .grid(row=1, column=1)
button9 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='9', bg='white', command=lambda:click_button(9)) .grid(row=1, column=2)
addition = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                  text='+', bg='white', command=lambda:click_button("+")) .grid(row=1, column=3)
button4 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='4', bg='white', command=lambda:click_button(4)) .grid(row=2, column=0)
button5 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='5', bg='white', command=lambda:click_button(5)) .grid(row=2, column=1)
button6 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='6', bg='white', command=lambda:click_button(6)) .grid(row=2, column=2)
subtraction = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                     text='-', bg='white', command=lambda:click_button("-")) .grid(row=2, column=3)
button1 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='1', bg='white', command=lambda:click_button(1)) .grid(row=3, column=0)
button2 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='2', bg='white', command=lambda:click_button(2)) .grid(row=3, column=1)
button3 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='3', bg='white', command=lambda:click_button(3)) .grid(row=3, column=2)
multiplication = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                        text='x', bg='white', command=lambda:click_button("*")) .grid(row=3, column=3)
button0 = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='0', bg='white', command=lambda:click_button(0)) .grid(row=4, column=0)
buttonClr = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='C', bg='white', command=click_clear_button) .grid(row=4, column=1)
buttonEquals = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                 text='=', bg='white', command=click_equal_button) .grid(row=4, column=2)
division = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                     text='÷', bg='white', command=lambda:click_button("/")) .grid(row=4, column=3)

root.mainloop()
