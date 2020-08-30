import os
import time
from random import randint

def main():
    print('\nText-Based Animation - Main Menu')
    print(' > Option 1: Flying Rocket')
    print(' > Option 2: Typewriter')
    print(' > Option 3: Rolling Die')
    print(' > Option 4: Space Invader')
    print(' > Option 5: Exit\n')

    option = input('Choose an option between 1 and 3: ')
    if option == "1":
        animate_rocket()
    elif option == "2":
        text = input('Add the text you want to animate: ')
        animate_text(text)
    elif option == "3":
        animate_die()
    elif option == "4":
        animate_spaceinvader()
    elif option == "5":
        print('Thank you for using this program.')
        exit()
    else:
        print('Invalid option!')
    repeat()

def repeat():
    choice = input("\nPress '1' to use the program again and '2' to exit: ")
    if choice == "1":
        main()
    if choice == "2":
        exit()

def animate_rocket():
    distanceFromTop = 20
    while True:
        print("\n" * distanceFromTop)
        print("          /\        ")
        print("          ||        ")
        print("          ||        ")
        print("         /||\        ")
        time.sleep(0.2)
        os.system('clear')
        distanceFromTop -= 1
        if distanceFromTop < 0:
            distanceFromTop = 20

def animate_text(text):
    numberOfCharacters = 1
    while True:
        print("\n")
        print(text[0:numberOfCharacters])
        numberOfCharacters += 1
        if numberOfCharacters > len(text):
            numberOfCharacters = 0
        time.sleep(0.2)
        os.system('clear')

die     = ["   \n O \n   "]   #1
die.append("  O\n   \nO  ")   #2
die.append("O  \n O \n  O")   #3
die.append("O O\n   \nO O")   #4
die.append("O O\n O \nO O")   #5
die.append("O O\nO O\nO O")   #6

def animate_die():
  for roll in range(0,15):
    os.system('clear')
    print("\n")
    number = randint(0,5)
    print(die[number])
    time.sleep(0.2)

def animate_spaceinvader():
  distanceFromTop = 0
  distanceFromLeftSide = 0
  step = 1
  while True:
    print("\n" * distanceFromTop)
    print((" " * distanceFromLeftSide) + "_^_")
    print((" " * distanceFromLeftSide) + "/|\\")
    distanceFromLeftSide +=step
    if distanceFromLeftSide>20 or distanceFromLeftSide<=0:
      step = -step
      distanceFromTop += 2
      if distanceFromTop >20:
        distanceFromTop = 0
        distanceFromLeftSide = 0
        step = 1
    time.sleep(0.05)
    os.system('clear')

main()
