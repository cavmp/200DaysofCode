from tkinter import *
import random
import time

root = Tk()
root.geometry('1100x700+0+0')
root.title('Restaurant Management System')

text_input = StringVar()
operator = ""

top_frame = Frame(root, width=1600, height=50, bg='#557A95', relief=SUNKEN)
top_frame.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
# Time
localtime = time.asctime(time.localtime(time.time()))
# Info
lblInfo = Label(top_frame, font=('arial', 50, 'bold'), text='Restaurant Management Systems', fg='steel blue', bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(top_frame, font=('arial', 20, 'bold'), text=localtime, fg='steel blue', bd=10, anchor='w')
lblInfo.grid(row=1, column=0)
# Calculator
def btn_click(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def btn_clear():
    global operator
    operator=""
    text_input.set("")

def btn_equals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

def Ref():
    x = random.randint(10908, 500876)
    random_ref = str(x)
    rand.set(random_ref)

    CoF = float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger = float(Burger.get())
    CoChicBurger = float(Chicken_Burger.get())
    CoCheeseBurger = float(Cheese_Burger.get())

    CostofFries = CoF * 60
    CostofDrinks = CoD * 75
    CostofFilet = CoFilet * 130
    CostofBurger = CoBurger * 130
    CostChickenBurger = CoChicBurger * 120
    CostCheese_Burger = CoCheeseBurger * 120

    CostofMeal = "P", str('%.2f' % (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostChickenBurger + CostCheese_Burger))

    PayTax = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostChickenBurger
               + CostCheese_Burger) * 0.12)

    TotalCost = (CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostChickenBurger + CostCheese_Burger)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostChickenBurger
               + CostCheese_Burger)/99)

    Service = "P", str('%.2f' % Ser_Charge)
    OverallCost = "P", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "P", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverallCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")


txt_display = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_input,bd=30, insertwidth=4,
                    bg='#557A95', justify='right')
txt_display.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='7',
              bg='#557A95', command=lambda: btn_click(7)) .grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='8',
              bg='#557A95', command=lambda: btn_click(8)) .grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='9',
              bg='#557A95', command=lambda: btn_click(9)) .grid(row=2, column=2)

Addition = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+',
              bg='#557A95', command=lambda: btn_click('+')) .grid(row=2, column=3)

btn4 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4',
              bg='#557A95', command=lambda: btn_click(4)) .grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5',
              bg='#557A95', command=lambda: btn_click(5)) .grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6',
              bg='#557A95', command=lambda: btn_click(6)) .grid(row=3, column=2)

Subtraction = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-',
              bg='#557A95', command=lambda: btn_click('-')) .grid(row=3, column=3)

btn1 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1',
              bg='#557A95', command=lambda: btn_click(1)) .grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2',
              bg='#557A95', command=lambda: btn_click(2)) .grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3',
              bg='#557A95', command=lambda: btn_click(3)) .grid(row=4, column=2)

Multiplication = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='x',
              bg='#557A95', command=lambda: btn_click('*')) .grid(row=4, column=3)

btn0 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0',
              bg='#557A95', command=lambda: btn_click(0)) .grid(row=5, column=0)

btnClr = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='C',
              bg='#557A95', command=btn_clear) .grid(row=5, column=1)

btnEquals = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='=',
              bg='#557A95', command=btn_equals) .grid(row=5, column=2)

Division = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='÷',
              bg='#557A95', command=lambda: btn_click('/')) .grid(row=5, column=3)

# Restaurant Info 1

rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()

lbl_reference = Label(f1, font=('arial', 16, 'bold'), text='Reference', bd=16, anchor='w')
lbl_reference.grid(row=0, column=0)
txt_reference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg='#ffffff', justify='right')
txt_reference.grid(row=0, column=1)

lbl_fries = Label(f1, font=('arial', 16, 'bold'), text='Large Fries', bd=16, anchor='w')
lbl_fries.grid(row=1, column=0)
txt_fries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg='#557A95', justify='right')
txt_fries.grid(row=1, column=1)

lbl_burger = Label(f1, font=('arial', 16, 'bold'), text='Burger Meal', bd=16, anchor='w')
lbl_burger.grid(row=2, column=0)
txt_burger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg='#557A95', justify='right')
txt_burger.grid(row=2, column=1)

lbl_filet = Label(f1, font=('arial', 16, 'bold'), text='Filet-o-Meal', bd=16, anchor='w')
lbl_filet.grid(row=3, column=0)
txt_filet = Entry(f1, font=('arial', 16, 'bold'), textvariable=Filet, bd=10, insertwidth=4, bg='#557A95', justify='right')
txt_filet.grid(row=3, column=1)

lbl_chicken = Label(f1, font=('arial', 16, 'bold'), text='Chicken Meal', bd=16, anchor='w')
lbl_chicken.grid(row=4, column=0)
txt_chicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Burger, bd=10, insertwidth=4, bg='#557A95', justify='right')
txt_chicken.grid(row=4, column=1)

lbl_cheese = Label(f1, font=('arial', 16, 'bold'), text='Cheese Meal', bd=16, anchor='w')
lbl_cheese.grid(row=5, column=0)
txt_cheese = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cheese_Burger, bd=10, insertwidth=4, bg='#557A95', justify='right')
txt_cheese.grid(row=5, column=1)

# Restaurant Info 2
lbl_drinks = Label(f1, font=('arial', 16, 'bold'), text='Drinks', bd=16, anchor='w')
lbl_drinks.grid(row=0, column=2)
txt_drinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg='#557A95', justify='right')
txt_drinks.grid(row=0, column=3)

lbl_cost = Label(f1, font=('arial', 16, 'bold'), text='Cost of Meal', bd=16, anchor='w')
lbl_cost.grid(row=1, column=2)
txt_cost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg='#ffffff', justify='right')
txt_cost.grid(row=1, column=3)

lbl_service = Label(f1, font=('arial', 16, 'bold'), text='Service Charge', bd=16, anchor='w')
lbl_service.grid(row=2, column=2)
txt_service = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4, bg='#ffffff', justify='right')
txt_service.grid(row=2, column=3)

lbl_tax = Label(f1, font=('arial', 16, 'bold'), text='State Tax', bd=16, anchor='w')
lbl_tax.grid(row=3, column=2)
txt_tax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg='#ffffff', justify='right')
txt_tax.grid(row=3, column=3)

lbl_subtotal = Label(f1, font=('arial', 16, 'bold'), text='Sub Total', bd=16, anchor='w')
lbl_subtotal.grid(row=4, column=2)
txt_subtotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg='#ffffff', justify='right')
txt_subtotal.grid(row=4, column=3)

lbl_total_cost = Label(f1, font=('arial', 16, 'bold'), text='Total Cost', bd=16, anchor='w')
lbl_total_cost.grid(row=5, column=2)
txt_total_cost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg='#ffffff', justify='right')
txt_total_cost.grid(row=5, column=3)

#Buttons
btn_total = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                   text='Total', bg='#557A95', command=Ref) .grid(row=7, column=1)

btn_reset = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                   text='Reset', bg='#557A95', command=Reset) .grid(row=7, column=2)

btn_exit = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                   text='Exit', bg='#557A95', command=qExit) .grid(row=7, column=3)

root.mainloop()
