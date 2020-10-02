# Take input from the user
user_input = input("Enter words you want to be alphabetized: ")

# breakdown the string into a list of words
words = user_input.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
