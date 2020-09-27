from tkinter import *
from tkinter import messagebox
import random
from collections import deque
import time

class Minesweeper:
    def __init__(self, master, size):
        self.SIZE = size
        self.d = [-(self.SIZE - 1), -self.SIZE, -(self.SIZE + 1), -1, 1, self.SIZE - 1, self.SIZE, self.SIZE + 1]
        # import images
        self.tile_plain = PhotoImage(file="images/tile_plain.gif")
        self.tile_clicked = PhotoImage(file="images/tile_clicked.gif")
        self.tile_mine = PhotoImage(file="images/tile_mine.gif")
        self.tile_flag = PhotoImage(file="images/tile_flag.gif")
        self.tile_wrong = PhotoImage(file="images/tile_wrong.gif")
        self.tile_no = []
        for x in range(1, 9):
            self.tile_no.append(PhotoImage(file="images/tile_" + str(x) + ".gif"))

        # set up frame
        frame = Frame(master)
        frame.pack()

        # solve button at bottom
        self.solve_btn = Button(frame, text="Solve")
        self.solve_btn.grid(row=3 + self.SIZE, column=0, columnspan=self.SIZE)
        self.solve_btn.configure(command=self.Solve)

        # create flag and clicked tile variables
        self.flags = 0
        self.correct_flags = 0
        self.clicked = 0

        # create buttons
        self.buttons = dict({})
        self.mines = 0
        x_coord = 1
        y_coord = 0
        for x in range(0, self.SIZE * self.SIZE):
            mine = 0
            gfx = self.tile_plain
            if random.uniform(0.0, 1.0) < 0.1:
                mine = 1
                self.mines += 1
            self.buttons[x] = [Button(frame, image=gfx), mine, 0, x, [x_coord, y_coord], 0]
            self.buttons[x][0].bind('<Button-1>', self.lclick_action(x))
            self.buttons[x][0].bind('<Button-3>', self.rclick_action(x))

            y_coord += 1
            if y_coord == self.SIZE:
                y_coord = 0
                x_coord += 1

        for key in self.buttons:
            self.buttons[key][0].grid(row=self.buttons[key][4][0], column=self.buttons[key][4][1])

        for key in self.buttons:
            nearby_mines = 0
            for j in self.d:
                if self.check_for_mines(key + j):
                    if self.validate(key, key + j):
                        nearby_mines += 1

            self.buttons[key][5] = nearby_mines

        self.label2 = Label(frame, text="Mines: " + str(self.mines))
        self.label2.grid(row=self.SIZE + 2, column=0, columnspan=self.SIZE)

    def validate(self, key, boomb):
        if boomb > self.SIZE * self.SIZE - 1 or boomb < 0:
            return False
        if boomb % self.SIZE == self.SIZE - 1 and key % self.SIZE == 0:
            return False
        if key % self.SIZE == self.SIZE - 1 and boomb % self.SIZE == 0:
            return False
        return True

    def check_for_mines(self, key):
        try:
            if self.buttons[key][1] == 1:
                return True
        except KeyError:
            pass

    def lclick_action(self, x):
        return lambda Button: self.left_click(self.buttons[x])

    def rclick_action(self, x):
        return lambda Button: self.right_click(self.buttons[x])

    def left_click(self, button_data):
        self.__clicked = button_data
        if button_data[1] == 1:

            for key in self.buttons:
                if self.buttons[key][1] != 1 and self.buttons[key][2] == 2:
                    self.buttons[key][0].config(image=self.tile_wrong)
                if self.buttons[key][1] == 1 and self.buttons[key][2] != 2:
                    self.buttons[key][0].config(image=self.tile_mine)

            self.endgame()
        else:

            if button_data[5] == 0:
                button_data[0].config(image=self.tile_clicked)
                self.clear_empty_boxes(button_data[3])
            else:
                button_data[0].config(image=self.tile_no[button_data[5] - 1])

            if button_data[2] != 1:
                button_data[2] = 1
                self.clicked += 1
            if self.clicked == self.SIZE * self.SIZE - self.mines:
                self.victory()

    def right_click(self, button_data):

        if button_data[2] == 0:
            button_data[0].config(image=self.tile_flag)
            button_data[2] = 2
            button_data[0].unbind('<Button-1>')

            if button_data[1] == 1:
                self.correct_flags += 1
            self.flags += 1

        elif button_data[2] == 2:
            button_data[0].config(image=self.tile_plain)
            button_data[2] = 0
            button_data[0].bind('<Button-1>', self.lclick_action(button_data[3]))

            if button_data[1] == 1:
                self.correct_flags -= 1
            self.flags -= 1

    def check_empty(self, key, queue):
        try:
            if self.buttons[key][2] == 0:
                if self.buttons[key][5] == 0:
                    self.buttons[key][0].config(image=self.tile_clicked)
                    queue.append(key)
                else:
                    self.buttons[key][0].config(image=self.tile_no[self.buttons[key][5] - 1])
                self.buttons[key][2] = 1
                self.clicked += 1
        except KeyError:
            pass

    def clear_empty_boxes(self, main_key):
        queue = deque([main_key])

        while len(queue) != 0:
            key = queue.popleft()
            for j in self.d:
                if self.validate(key, key + j):
                    self.check_empty(key + j, queue)

    def endgame(self):
        messagebox.showinfo("Game Over", "You Lose!")
        global root
        sys.exit()
        root.destroy()

    def victory(self):
        messagebox.showinfo("Game Over", "You Win!")
        global root
        sys.exit()
        root.destroy()

    def Solve(self):
        Solved = False
        while not Solved:
            ran = int(random.uniform(0, self.SIZE - 1))
            self.left_click(self.buttons[ran])
            if self.__clicked[1] == 1:
                messagebox.showinfo("Sorry!", "Not Lucky")
            if self.__clicked[5] == 0:
                i = 0
                f = False
                while True:
                    if i == self.SIZE * self.SIZE:
                        if f:
                            i = 0
                            f = False
                        else:
                            messagebox.showinfo("Sorry!", "I can't Solve it Help ME")
                            Solved = True
                            break
                    if self.operation(i):
                        f = True
                    i += 1

    def operation(self, key):
        notclicked = 0
        flagged = 0
        notclickedlist = range(8)
        for j in self.d:
            if self.validate(key, key + j):
                if self.buttons[key + j][2] == 0:
                    notclickedlist[notclicked] = key + j
                    notclicked += 1
                elif self.buttons[key + j][2] == 2:
                    flagged += 1

        global root
        if self.buttons[key][5] == notclicked + flagged:
            x = 0
            while x < notclicked:
                self.right_click(self.buttons[notclickedlist[x]])
                x += 1
                root.update()
                time.sleep(1)
                return True
        if self.buttons[key][5] == flagged:
            x = 0
            while x < notclicked:
                self.left_click(self.buttons[notclickedlist[x]])
                x += 1
                root.update()
                time.sleep(1)
                return True
        return False


def main():
    global root
    size = int(input("Enter Size = "))
    root = Tk()

    root.title("Minesweeper Robot Project ")

    minesweeper = Minesweeper(root, size)

    root.mainloop()


if __name__ == "__main__":
    main()
