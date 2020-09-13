import random

# to replace all "-" (empty characters) with a random letter
def randomFill(wordsearch):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for row in range(0, 12):
        for col in range(0, 12):
            if wordsearch[row][col] == "-":
                randomLetter = random.choice(LETTERS)
                wordsearch[row][col] = randomLetter

# to output the wordsearch on screen
def displayWordsearch(wordsearch):
    print(" _________________________")
    print("|                         |")
    for row in range(0, 12):
        line = "| "
        for col in range(0, 12):
            line = line + wordsearch[row][col] + " "
        line = line + "|"
        print(line)
    print("|_________________________|")

# to add a word to the wordsearch at a random position
def addWord(word, wordsearch):
    row = random.randint(0, 11)
    col = 0
    for i in range(0, len(word)):
        wordsearch[row][col + i] = word[i]

# Create an empty 12 by 12 wordsearch (list of lists)
wordsearch = []
for row in range(0, 12):
    wordsearch.append([])
    for col in range(0, 12):
        wordsearch[row].append("-")

# Adding words to our wordsearch
addWord("PYTHON", wordsearch)
addWord("ALGORITHM", wordsearch)
addWord("CODING", wordsearch)
addWord("PROGRAM", wordsearch)
addWord("PROJECT", wordsearch)
addWord("COMPUTER", wordsearch)
# You can add more words here

# All unused spaces in the wordsearch will be replaced with a random letter
randomFill(wordsearch)

# Display the fully competed wordseach on screen
displayWordsearch(wordsearch)

print('There are 6 words you need to guess.')

words_guessed = 0

while words_guessed < 6:
    words = input('\nInput a word you can see: ')

    if words == 'python':
        words_guessed += 1
        print('Score:',words_guessed)
    elif words == 'algorithm':
        words_guessed += 1
        print('Score:',words_guessed)
    elif words == 'coding':
        words_guessed += 1
        print('Score:',words_guessed)
    elif words == 'program':
        words_guessed += 1
        print('Score:',words_guessed)
    elif words == 'project':
        words_guessed += 1
        print('Score:',words_guessed)
    elif words == 'computer':
        words_guessed += 1
        print('Score:',words_guessed)
    else:
        words_guessed += 0
        print('Wrong word! Try again.')

print("\nCongratulations! You've found all the words!")
