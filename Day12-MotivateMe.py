import random
from tkinter import Tk, Label, Button

class MotivateMe:
    def __init__(self, master):
        self.master = master
        master.title("Motivate Me") # GUI's title

        self.label = Label(master, text="Press 'Motivate Me' to get your inspirational quote for today!")
        self.label.pack()

        self.quote_button = Button(master, text="Motivate Me!", command=self.quote)
        self.quote_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def quote(self):
        rand_num = random.randint(1, 10) # Will generate a random quote assigned to a number

        if rand_num == 1:
            print('"Who you are is defined by what youre willing to struggle for." - Mark Manson')
        if rand_num == 2:
            print('"Whether you think you can, or you think you cant - youre right." - Henry Ford')
        if rand_num == 3:
            print('"If you create a vision for yourself and stick with it, you can make amazing things happen in your '
                  'life. Once you have done the work to create the clear vision, it is the discipline and effort to '
                  'maintain that vision that can make it all come true." - Pete Carroll')
        if rand_num == 4:
            print('"To be gritty is to keep putting one foot in front of the other. To be gritty is to hold fast to an '
                  'interesting and purposeful goal. To be gritty is to invest, day after week after year, in '
                  'challenging practice. To be gritty is to fall down seven times, and rise eight." - Angela Duckworth')
        if rand_num == 5:
            print('“Your life is yours to create. Be grateful for the opportunity. Seize it with passion and boldness.'
                  ' Whatever you decide to do, commit to it with all your strength … and begin it now.” - Peter Buffett')
        if rand_num == 6:
            print('"If you do what you always did, you will get what you always got."')
        if rand_num == 7:
            print('"Success is the sum of small efforts, repeated day-in and day-out." - Robert Collier')
        if rand_num == 8:
            print('“The only person you should try to be better than, is the person you were yesterday.” - Matty Mullens')
        if rand_num == 9:
            print('“Nothing will work unless you do.” - Maya Angelou')
        if rand_num == 10:
            print('“Whatever the mind of man can conceive and believe, it can achieve.” - Napoleon Hill')

root = Tk()
my_gui = MotivateMe(root)
root.mainloop()

