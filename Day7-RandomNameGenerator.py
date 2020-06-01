import random

def main():
    """
    Growing up, my teachers always used this website wherein the computer randomizes the students. After coding
    a random number generator, I decided to make another program that would randomize names given by the user. 
    """
    name_list = [] # Starts off as an empty list as the user hasn't inputted any names
    while True: # While the user hasn't pressed 'enter'
        name = input("Add name here. Press 'enter' when done adding: ")
        if name == '': 
            break
        name_list.append(name) # The names the user added will be put in the empty list

    print("Here is your list in random order:")
    for i in range(len(name_list)):
        random_name_generator = random.choice(name_list) # This randomizes the arrangement of names in the list
        print(random_name_generator) # Gives the randomized list to user

# This provided line is required at the end of a Python file to call the main() function.
if __name__ == '__main__':
    main()
