import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

no_of_cards = input('\nHow many cards do you need?\nOnly input 5, 10, 15, or 20: ')

print("\nYou got:")

if no_of_cards == "5":
    for i in range(5):
        print(deck[i][0], "of", deck[i][1])

if no_of_cards == "10":
    for i in range(10):
        print(deck[i][0], "of", deck[i][1])

if no_of_cards == "15":
    for i in range(15):
        print(deck[i][0], "of", deck[i][1])

if no_of_cards == "20":
    for i in range(20):
        print(deck[i][0], "of", deck[i][1])
