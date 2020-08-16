def encryption(b, f):
    cipher = ""
    print(b)
    for i in b:
        if i.isalpha():
            Alphabet = ord(i) + f
            if Alphabet > ord("z"):
                Alphabet -= 26
        Letter = chr(Alphabet)
        cipher += Letter
    print(cipher)

    p = input("\nWould you like to do another (yes or no): ")

    if p == "yes":
        main()
    elif p == "no":
        exit()


def decryption(c, g):
    decryptiontext = ""

    for i in c:
        if i.isalpha():
            Alphabet = ord(i) - g
            if Alphabet < ord("Z"):
                Alphabet += 26
        Letter = chr(Alphabet)
        decryptiontext += Letter
    print(decryptiontext)

    p = input("\nWould you like to do another (yes or no): ")

    if p == "yes":
        main()
    elif p == "no":
        exit()


def main():
    a = input("\nWould to like to encrypt or decrypt: ")

    e = input("\nWhat would you like to encrypt or decrypt: ")

    d = int(input("\nHow much encryption/decryption would you want (please enter a number) : "))

    if a == "encrypt":
        encryption(e, d)

    elif a == "decrypt":
        decryption(e, d)


main()
