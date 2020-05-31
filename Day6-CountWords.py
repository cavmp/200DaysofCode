def main():
    user_input = input("Paste here to count words: ")
    count = 0
    for line in user_input:
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            count +=1 
    print("Your input contains " + str(count) + " words")

if __name__ == '__main__':
    main()
