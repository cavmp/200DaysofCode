import random

"""
These constants were implemented as they will be used throughout the code. Furthermore, it will be easier for me to 
change these if I want to try different numbers. 
"""
NUM_MIN = 10 # The assignment requires a minimum number of 99 which will be used in the code below
NUM_MAX = 99 # The assignment requires a maximum number of 99 which will be used in the code below
MAXIMUM_CORRECT = 3 # The assignment requires the user to get 3 problems correct in a row

def main():
    """
    I did this code after learning Python's control flows and I applied a lot of my code here from that.
    First, I started coding as a whole. I decomposed the code to 2 main functions: addition_question and
    ending_statement. Then, I moved on to define each functions to make an addition game.
    """
    addition_questions() # Randomly generates addition problems for the user and checks the answer from the user
    ending_statement() # Closing statement for when the user gets 3 questions in a row

def addition_questions():
    correct_answers = 0 # To start, user has 0 correct answers
    while correct_answers < 3: # To guarantee that the user has 3 correct answers in a row
        num1 = random.randint(NUM_MIN, NUM_MAX) # Will generate a random number from num_min to num_max
        num2 = random.randint(NUM_MIN, NUM_MAX) # Will generate another random number from num_min to num_max
        real_answer = num1 + num2 # Real answer of the addition question will go here
        print("What is " + str(num1) + " + " + str(num2) + "? ")
        user_answer = int(input("Your answer: ")) # User's answer in the terminal
        if real_answer != user_answer: # A condition for when the real answer does not equal to the user's answer
            print("Incorrect, the answer is " + str(real_answer) + ".") # Will tell the user the correct answer
            correct_answers = 0 # Restarts answers correct to 0 so the while loop also restarts
        else: # A condition for when the real answer is equal to the user's answer
            correct_answers += 1 # Adds 1 to answers correct
            print("Correct! " + "You've gotten " + str(correct_answers) + " correct in a row.")
            # Informs the user his/her numbers of correct answers in a row

def ending_statement():
    print("Congratulations! You mastered addition.") # The ending statement will be printed in the terminal

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
