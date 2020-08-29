def main():
    print('\nTemperature Converter - Main Menu')
    print(' > Option 1: Convert from Celsius to Fahrenheit')
    print(' > Option 2: Convert fro Fahrenheit to Celsius')
    print(' > Option 3: Exit\n')

    option = input('Choose an option between 1 and 3: ')
    if option == "1":
        celsius = int(input('Type a temperature in degree Celsius: '))
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature:", fahrenheit, "degrees Fahrenheit")
    elif option == "2":
        fahrenheit = int(input('Type a temperature in degrees Fahrenheit: '))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature:", celsius, "degrees Celsius")
    elif option == "3":
        print('Thank you for using this program.')
        exit()
    else:
        print('Invalid option!')
    repeat()

def repeat():
    choice = input("\nPress '1' to use the program again and '2' to exit: ")
    if choice == "1":
        main()
    if choice == "2":
        exit()

main()
