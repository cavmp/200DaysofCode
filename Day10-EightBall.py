"""
This is a program that will simulate a magic eight ball. The program prompts the user to type a yes or no question and gives a
random answer from a set of predetermined answers.
"""

import random

def main():
    while True:
        # 1  Prompt user for a yes or no question
        user_input = input("Ask a yes or no question: ")
        if user_input == "": # User will press 'enter' when done playing
            break
        # 2 Print a random number from pre-set list of answers
        print_random_answer()

def print_random_answer():
    # 1) pick a random integer from 1 to 6 (inclusive)
    rand_num = random.randint(1, 6)
    # if this number is equal to 1:
    # print "No chance"
    if rand_num == 1:
        print("Cannot predict now")

    if rand_num == 2:
        print("As I see it, yes")

    if rand_num == 3:
        print("Better not tell you now")

    if rand_num == 4:
        print("My sources says no")

    if rand_num == 5:
        print("Most likely")

    if rand_num == 6:
        print("Not a chance")


if __name__ == '__main__':
    main()
