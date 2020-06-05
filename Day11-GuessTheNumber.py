import random

def main():
    secret_number = random.randint(1, 100) # The program will get a random integer from 1 - 100
    print("I am thinking of a number between 1 and 100") 
    print("You have 15 tries to guess the number")

    for i in range(15): # The user has a maximum of 15 guesses
        print("Take a guess.")
        guess = int(input())

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        elif guess == secret_number:
            print("Good job! You guessed my number in " + str(i) + " guesses!")
            break # Breaks the 'for loop'

if __name__ == '__main__':
    main()
