import time
import random

QUIZ_TIME = 30

def information_storage():
    # Asks the user for name and definition of a certain concept. Note that this program is case sensitive
    dictionary = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        definition = input("Definition: ")
        dictionary[name] = definition
        print("") # Adds a space in between
    return dictionary

def print_dictionary(dictionary):
    # Prints out all the inputted names of the concepts
    print("Here is the complete list of your dictionary:")
    for name in dictionary:
        print(name, ':', dictionary[name])
    print("")  # Adds a space in between

def lookup_dictionary(dictionary):
    while True:
        name = input("Enter concept to lookup: ")
        if name == "":
            break
        if name not in dictionary:
            print(name + " is not included")
            print("")  # Adds a space in between
        else:
            print(name + " is " + dictionary[name])
            print("") # Adds a space in between

def quiz(definition):
    # Runs a quiz
    print("")  # Adds a space in between
    print("It's time to test your memory!")
    print("You will now be asked for the names of the given definition")
    print("Answer as many as you can within " + str(QUIZ_TIME) + " seconds.")

    start = time.time()
    end = time.time()
    tracker = 0
    while end-start < QUIZ_TIME + 1:
        if run_quiz(definition):
            tracker += 1
        else:
            tracker =+ 0
        end = time.time()
    return tracker

def run_quiz(definition):
    definition_list = list(definition.keys())
    random_word = random.choice(definition_list)
    real_answer = definition.get(random_word)
    user_answer = input("What is a " + str(random_word) + "? ")
    if user_answer == real_answer:
        print('Correct!')
        return True
    else:
        print('Correct answer is', real_answer)
        return False


def main():
    print("Note that this program is case sensitive")
    definition = information_storage()
    print_dictionary(definition)
    lookup_dictionary(definition)
    correct_answer = quiz(definition)
    print("")  # Adds a space in between
    print('You were correct ' + str(correct_answer) + " time/s.")


if __name__ == '__main__':
    main()
