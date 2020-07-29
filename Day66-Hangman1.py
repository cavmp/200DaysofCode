import random

WORD_LIST = ['book', 'computer', 'phone', 'spiderman', 'plastic', 'cookies', 'lasagna', 'pizza', 'pasta', 'basketball',
             'volleyball', 'wine', 'apple']


def main():
    word = choose_word()

    # draws the initial game board.
    print('')
    print('    ---------')
    print('    |       |')
    print('            |')
    print('            |')
    print('            |')
    print('            |')
    print('            |')
    print('            |')
    print('-----------------')

    spaced_word = correct_spacing(word)
    play_game(word, spaced_word)
    print('The word was ' + word)

# Randomly selects a word from the list
def choose_word():
    a = random.randint(0, 10)
    return WORD_LIST[a]

def correct_spacing(a):
    # returns the letters of the word with spaces in between them.
    b = ''
    for i in range(len(a)):
        b += a[i] + ' '
    return b

# main game loop that takes in the users guess and prints the corresponding hangman board.

def play_game(a, b):
    # prints the spaces representing the word
    blank_spaces = ''
    for i in range(len(a)):
        blank_spaces += '_ '
    print(blank_spaces)
    print('')
    print('')

    # asks user to guess letter
    body_parts = 0  # variable that tracks the number of incorrect guesses.
    while blank_spaces != b and body_parts < 6:
        guess_tracker = ''  # variable that holds the string for the current round
        guess = input('Guess a letter: ')

        for i in range(len(b)):  # builds the string letter/blank by letter/blank.
            if blank_spaces[i] != b[i]:  # if user hasn't already guessed this space correctly.
                if guess == b[i]:  # user guess matches the space.
                    guess_tracker += b[i]
                else:  # user guess doesn't match the space.
                    guess_tracker += blank_spaces[i]
            else:  # user has already guessed this space correctly.
                guess_tracker += blank_spaces[i]
        if guess_tracker == blank_spaces:  # this means the guess was incorrect (didn't match any spaces)
            body_parts += 1
        draw_board(body_parts)
        blank_spaces = guess_tracker
        print(blank_spaces)
        print('')
    if body_parts < 6:
        print('You Won!')
    else:
        print('GAMEOVER')


# draws the hangman board


def draw_board(a):
    # prints the noose
    noose_1 = '    ---------'
    noose_2 = '    |       |'
    noose_3 = '            |'
    noose_4 = '            |'
    noose_5 = '            |'
    noose_6 = '            |'
    noose_7 = '            |'
    noose_8 = '            |'
    noose_9 = '-----------------'

    head_3 = '   ( )      |'
    body_4 = '    |       |'
    body_5 = '    |       |'
    body_6 = '    |       |'
    left_arm_3 = ' \ ( )      |'
    left_arm_4 = '  \ |       |'
    right_arm_3 = ' \ ( ) /    |'
    right_arm_4 = '  \ | /     |'
    left_leg_7 = '  /         |'
    left_leg_8 = ' /          |'
    right_leg_7 = '  /   \     |'
    right_leg_8 = ' /     \    |'

    print(noose_1)
    print(noose_2)
    if a == 0:
        print(noose_3)
        print(noose_4)
        print(noose_5)
        print(noose_6)
        print(noose_7)
        print(noose_8)
    elif a == 1:
        print(head_3)
        print(noose_4)
        print(noose_5)
        print(noose_6)
        print(noose_7)
        print(noose_8)
    elif a == 2:
        print(head_3)
        print(body_4)
        print(body_5)
        print(body_6)
        print(noose_7)
        print(noose_8)
    elif a == 3:
        print(left_arm_3)
        print(left_arm_4)
        print(body_5)
        print(body_6)
        print(noose_7)
        print(noose_8)
    elif a == 4:
        print(right_arm_3)
        print(right_arm_4)
        print(body_5)
        print(body_6)
        print(noose_7)
        print(noose_8)
    elif a == 5:
        print(right_arm_3)
        print(right_arm_4)
        print(body_5)
        print(body_6)
        print(left_leg_7)
        print(left_leg_8)
    elif a == 6:
        print(right_arm_3)
        print(right_arm_4)
        print(body_5)
        print(body_6)
        print(right_leg_7)
        print(right_leg_8)
    print(noose_9)

if __name__ == '__main__':
    main()
