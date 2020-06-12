import random
from tkinter import Tk, Label, Button

class MotivateMe:
    def __init__(self, master):
        self.master = master
        master.title("Random Music!")

        self.label = Label(master, text="These aren't easy times, but a nice song can help.")
        self.label.pack()

        self.label = Label(master, text="Press 'Random Music' to get a link of a song!")
        self.label.pack()

        self.quote_button = Button(master, text="Random Music", command=self.quote)
        self.quote_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def quote(self):
        rand_num = random.randint(1, 10)

        if rand_num == 1:
            print('Post Malone - Circles: https://www.youtube.com/watch?v=wXhTHyIgQ_U')
        if rand_num == 2:
            print('Rex Orange County - Always: https://www.youtube.com/watch?v=HqYAgDYvdDw')
        if rand_num == 3:
            print('Tyler the Creator - See You Again: https://www.youtube.com/watch?v=TGgcC5xg9YI')
        if rand_num == 4:
            print('Bee Gees - How Deep Is Your Love: https://www.youtube.com/watch?v=XpqqjU7u5Yc')
        if rand_num == 5:
            print('Kid Cudi - Pursuit of Happiness: https://www.youtube.com/watch?v=7xzU9Qqdqww')
        if rand_num == 6:
            print('J. Cole - Love Yourz: https://www.youtube.com/watch?v=Ka4BxFizU7I')
        if rand_num == 7:
            print('J. Cole - 4 Your Eyes Only: https://www.youtube.com/watch?v=g_W9af_CQDs')
        if rand_num == 8:
            print('Brockhampton - Sugar: https://www.youtube.com/watch?v=sZd-t5-I5uA')
        if rand_num == 9:
            print('Sun Rai - San Francisco Street: https://www.youtube.com/watch?v=9zEl-FQLI4A')
        if rand_num == 10:
            print('Cuco, Clairo - Drown: https://www.youtube.com/watch?v=_1VyGyWpQpU')

root = Tk()
my_gui = MotivateMe(root)
root.mainloop()
