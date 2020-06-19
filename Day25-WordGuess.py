import random


WORD_LIST = ['book', 'computer', 'phone', 'spiderman', 'plastic', 'cookies', 'lasagna', 'pizza', 'pasta', 'basketball',
             'volleyball', 'wine', 'apple']
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    word = ''
    for i in range (0, len(secret_word)):
        word = word+"-"
    return word

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game. 
    """
    for word in WORD_LIST:
        words = word.strip()

    my_list = []
    my_list.append(words)
    secret_word = random.choice(my_list)
    return secret_word



def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    dashes = play_game(secret_word)
    length = len(secret_word)
    n = 0
    print('The word now looks like this: ' + str(dashes))
    print('You have ' + str(INITIAL_GUESSES) + ' guesses left')
    while secret_word != dashes:
        letter = input("Please guess a single letter: ")
        for i in range(0, length):
            if letter == secret_word[i]:
                dashes = dashes[:i] + letter + dashes[i + 1:]
            if "-" not in dashes:
                print("Congratulations. The word is: " + str(secret_word))
                break
        if letter.isalpha() and len(letter) == 1:
            if letter in secret_word:
                print("That guess is correct. The word is now " + dashes)
        if letter not in secret_word and len(letter) == 1:
            n = n + 1
            print("There are no " + str(letter) + "'s in this word")
            print("The word is now " + dashes)
            print("You have " + str(INITIAL_GUESSES - n) + " guesses left.")
        if n == INITIAL_GUESSES and secret_word == dashes:
            print("Congratulations.The word is: " + str(secret_word))
            break
        if n == INITIAL_GUESSES:
            print("Sorry you lost. The secret word was " + str(secret_word))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
