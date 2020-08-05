from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x600')
root.title('Discount Calculator')

title_lbl = Label(root, text='\nDiscount Calculator', font=('Times 30 bold'), fg='#4056a1') .pack(side=TOP)

price_frame = Frame(root)
price_frame.pack(side=TOP, pady=90)

price_lbl = Label(price_frame, text='Price', font=('Times 20'), fg='#f13c20') .pack(side=LEFT)
price_entry = Entry(price_frame, width=5)
price_entry.pack(side=LEFT)

discount_frame = Frame(root)
discount_frame.pack(side=TOP)

discount_lbl = Label(discount_frame, text='Sales Rate', font=('Times 20'), fg='#f13c20') .pack(side=LEFT)
discount_rate = Spinbox(discount_frame, from_=0, to=100, increment=5, width=5)
discount_rate.pack(side=LEFT)

def CalculateDiscount():
    price = float(price_entry.get())
    discount = float(discount_rate.get())
    total_price = price - ((discount / 100) * price)
    total_price_text = "The total price with tax is: " + str(total_price)
    messagebox.showinfo("Total Price", total_price_text)

calculate = Button(root, text='Calculate Tax', command=CalculateDiscount) .pack(side=TOP, pady=100)

root.mainloop()
