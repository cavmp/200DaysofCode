password = input("\nType your password: ")
score = 0

# Check the password for specific characters
lowercase = False
uppercase = False
number = False
punctuation = False
for c in password:
    if c in "abcdefghijklmnopqrstuvwxyz":
        lowercase = True
    if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True
    if c in "1234567890":
        number = True
    if c in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
        punctuation = True

# Check if password is atleast 8 characters long
if len(password) > 7:
    score += 5

# Check if password contains number/s and letters
if lowercase == True and uppercase == True and number == True:
    score += 10

# Check if password contains at least one punctuation sign
if punctuation == True:
    score += 5

# Check if password contains lowercase and uppercase characters
if lowercase == True and uppercase == True:
    score += 10

print("Your password's score is:", score, "/30\n")
