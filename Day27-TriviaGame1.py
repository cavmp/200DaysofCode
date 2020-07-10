from tkinter import *
import random

def main():
    root = Tk()
    root.title('Trivia Game!')
    width = 700
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Top = Frame(root, width=600) # This frame widget is used as a container widget to organize other widgets
    Top.pack(side=TOP)

    label = Label(root, font=("times new roman", 90), text="TRIVIA GAME")
    label.pack(side=TOP)

    instruction = Label(root, text="Press ▶ to be given a question. Note: Only use small letters for your answers")
    instruction.pack(side=TOP)

    Bottom = Frame(root, width=600)
    Bottom.pack(side=BOTTOM)

    triviaGame = TriviaGame(root)
    triviaGame.pack(side=BOTTOM)

    root.mainloop()

class TriviaGame(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)

        self.play_button = Button(self.master, text='▶', command=self.question, bg='white')
        self.play_button.pack()

        self.end_button = Button(self.master, text='EXIT', font=("times new roman", 10), command=self.Exit)
        self.end_button.pack(side=BOTTOM)

    def question(self):
        rand_num = random.randint(1, 20)
        if rand_num == 1:
            self.question1 = Label(self.master, text="What is the rarest M&M color?")
            self.question1.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer1)
            self.button.pack()
        if rand_num == 2:
            self.question2 = Label(self.master, text="In a website browser address bar, what does “www” stand for?")
            self.question2.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer2)
            self.button.pack()
        if rand_num == 3:
            self.question3 = Label(self.master, text="In what year were the first Air Jordan sneakers released?")
            self.question3.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer3)
            self.button.pack()
        if rand_num == 4:
            self.question4 = Label(self.master, text="In a game of bingo, which number is represented by the phrase “two little ducks”?")
            self.question4.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer4)
            self.button.pack()
        if rand_num == 5:
            self.question5 = Label(self.master, text="According to Greek mythology who was the first woman on earth?")
            self.question5.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer5)
            self.button.pack()
        if rand_num == 6:
            self.question6 = Label(self.master, text="Which planet is the hottest in the solar system?")
            self.question6.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer6)
            self.button.pack()
        if rand_num == 7:
            self.question7 = Label(self.master, text="In which European city would you find Orly airport?")
            self.question7.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer7)
            self.button.pack()
        if rand_num == 8:
            self.question8 = Label(self.master, text="Which singer’s real name is Stefani Joanne Angelina Germanotta?")
            self.question8.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer8)
            self.button.pack()
        if rand_num == 9:
            self.question9 = Label(self.master, text="Which author wrote the ‘Winnie-the-Pooh’ books?")
            self.question9.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer9)
            self.button.pack()
        if rand_num == 10:
            self.question10 = Label(self.master, text="Which Dutch artist painted “Girl with a Pearl Earring?")
            self.question10.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer10)
            self.button.pack()
        if rand_num == 11:
            self.question11 = Label(self.master, text="Which country consumes the most chocolate per capita?")
            self.question11.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer11)
            self.button.pack()
        if rand_num == 12:
            self.question12 = Label(self.master, text="What is the loudest animal on Earth?")
            self.question12.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer12)
            self.button.pack()
        if rand_num == 13:
            self.question13 = Label(self.master, text="What was the first toy to be advertised on television?")
            self.question13.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer13)
            self.button.pack()
        if rand_num == 14:
            self.question14 = Label(self.master, text="In which city was Anne Frank’s hiding place?")
            self.question14.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer14)
            self.button.pack()
        if rand_num == 15:
            self.question15 = Label(self.master, text="Which of Shakespeare’s plays is the longest?")
            self.question15.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer15)
            self.button.pack()
        if rand_num == 16:
            self.question16 = Label(self.master, text="What is the tallest breed of dog in the world?")
            self.question16.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer16)
            self.button.pack()
        if rand_num == 17:
            self.question17 = Label(self.master, text="How many ribs are in a human body?")
            self.question17.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer17)
            self.button.pack()
        if rand_num == 18:
            self.question18 = Label(self.master, text="What is the world’s biggest island?")
            self.question18.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer18)
            self.button.pack()

        if rand_num == 19:
            self.question19 = Label(self.master, text="Which country is known as the Land of White Elephant?")
            self.question19.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer19)
            self.button.pack()

        if rand_num == 20:
            self.question20 = Label(self.master, text=" What color eyes do most humans have?")
            self.question20.pack()
            self.user_entry = Entry(self.master)
            self.user_entry.pack()
            self.button = Button(self.master, text="Answer!", command=self.check_answer20)
            self.button.pack()


    def check_answer1(self):
        answer1 ='brown' or 'Brown' or 'BROWN'
        user_answer = self.user_entry.get()
        if answer1 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is brown.")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer2(self):
        answer2 ='world wide web' and 'World Wide Web' or 'WORLD WIDE WEB'
        user_answer = self.user_entry.get()
        if answer2 != user_answer:
            if answer2 != user_answer:
                self.incorrect = Label(self.master, text="Incorrect, the answer is World Wide Web.")
                self.incorrect.pack()
            else:
                self.correct = Label(self.master, text="Correct!")
                self.correct.pack()

    def check_answer3(self):
        answer3 = '1984'
        user_answer = self.user_entry.get()
        if answer3 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is 1984.")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer4(self):
        answer4 = '22'
        user_answer = self.user_entry.get()
        if answer4 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is 22.")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer5(self):
        answer5 = 'pandora' or 'Pandora' or 'PANDORA'
        user_answer = self.user_entry.get()
        if answer5 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Pandora")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer6(self):
        answer6 = 'venus' or 'Venus' or 'VENUS'
        user_answer = self.user_entry.get()
        if answer6 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Venus")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer7(self):
        answer7 = 'paris' or 'Paris' or 'PARIS'
        user_answer = self.user_entry.get()
        if answer7 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Paris.")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer8(self):
        answer8 = 'lady gaga' or 'LADY GAGA' or 'Lady Gaga'
        user_answer = self.user_entry.get()
        if answer8 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Lady Gaga.")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer9(self):
        answer9 = 'a. a. milne' or 'A. A. Milne' or 'Milne'
        user_answer = self.user_entry.get()
        if answer9 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is A. A. Milne.")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer10(self):
        answer10 = 'vermeer' or 'Vermeer' or'VERMEER'
        user_answer = self.user_entry.get()
        if answer10 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Vermeer")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer11(self):
        answer11 = 'switzerland' or 'Switzerland' or 'SWITZERLAND'
        user_answer = self.user_entry.get()
        if answer11 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Switzerland")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer12(self):
        answer12 = 'sperm whale' or 'Sperm whale' or 'The sperm whale' or 'the sperm whale'
        user_answer = self.user_entry.get()
        if answer12 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is the sperm whale")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer13(self):
        answer13 = 'mr. potato head' or 'Mr. Potato Head' or 'MR. POTATO HEAD'
        user_answer = self.user_entry.get()
        if answer13 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Mr. Potato Head")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer14(self):
        answer14 = 'amsterdam' or 'Amsterdam' or 'AMSTERDAM'
        user_answer = self.user_entry.get()
        if answer14 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Amsterdam")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer15(self):
        answer15 = 'hamlet' or 'HAMLET' or 'Hamlet'
        user_answer = self.user_entry.get()
        if answer15 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Hamlet")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer16(self):
        answer16 = 'the great dane' or 'The Great Dane' or 'THE GREAT DANE'
        user_answer = self.user_entry.get()
        if answer16 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is The Great Dane")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer17(self):
        answer17 = '24'
        user_answer = self.user_entry.get()
        if answer17 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is 24")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer18(self):
        user_answer = self.user_entry.get()
        answer18 = 'greenland' or 'GREENLAND' or 'Greenland'
        if answer18 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Greenland")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer19(self):
        user_answer = self.user_entry.get()
        answer19 = 'thailand' or 'THAILAND' or 'Thailand'
        if answer19 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is Thailand")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def check_answer20(self):
        user_answer = self.user_entry.get()
        answer20 = 'brown' or 'BROWN' or 'Brown'
        if answer20 != user_answer:
            self.incorrect = Label(self.master, text="Incorrect, the answer is brown")
            self.incorrect.pack()
        else:
            self.correct = Label(self.master, text="Correct!")
            self.correct.pack()

    def Exit(self):
        self.destroy()
        exit()

if __name__ == '__main__':
    main()
