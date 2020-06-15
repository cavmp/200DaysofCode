import random

def main():
    print('What is your bad habit?')
    user_input = input('My bad habit is that I ')
    print('You ' + user_input + '???')
    tough_love()

def tough_love():
    rand_reply = random.randint(1, 5)
    if rand_reply == 1:
        print('You should be ashamed of yourself!')
    if rand_reply == 2:
        print('I thought you were better than that...')
    if rand_reply == 3:
        print('My disapproval is overwhelming.')
    if rand_reply == 4:
        print("That's horrible!")
    if rand_reply == 5:
        print("That's terrible! You should really let go of that habit.")

if __name__ == '__main__':
    main()
