def main():
    user_input = input("Paste here to count words: ")
    word_length = len(user_input.split())
    print("Your input contains " + str(word_length) + " words")

if __name__ == '__main__':
    main()
