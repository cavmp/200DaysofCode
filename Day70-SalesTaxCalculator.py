from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x600')
root.title('Sales Tax Calculator')

title_lbl = Label(root, text='\nSales Tax Calculator', font=('Times 30 bold'), fg='#4056a1') .pack(side=TOP)

price_frame = Frame(root)
price_frame.pack(side=TOP, pady=90)

price_lbl = Label(price_frame, text='Price', font=('Times 20'), fg='#f13c20') .pack(side=LEFT)
price_entry = Entry(price_frame, width=5)
price_entry.pack(side=LEFT)

tax_frame = Frame(root)
tax_frame.pack(side=TOP)

tax_lbl = Label(tax_frame, text='Tax Rate', font=('Times 20'), fg='#f13c20') .pack(side=LEFT)
tax_rate = Spinbox(tax_frame, from_=0, to=100, increment=5, width=5)
tax_rate.pack(side=LEFT)

def CalculateTax():
    price = float(price_entry.get())
    tax = float(tax_rate.get())
    total_price = price + ((tax / 100) * price)
    total_price_text = "The total price with tax is: " + str(total_price)
    messagebox.showinfo("Total Price", total_price_text)

calculate = Button(root, text='Calculate Tax', command=CalculateTax) .pack(side=TOP, pady=100)

root.mainloop()
