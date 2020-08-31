def main():
    print('\nRadians/Degrees Converter - Main Menu')
    print('Choose one of the following options:')
    print('1 > Convert an angle from Radians to Degrees')
    print('2 > Convert an angle from Degrees to Radians')
    print('3 > Exit\n')

    user_choice = input('Select an option: ')
    if user_choice == '1':
        radians_to_degrees()
    elif user_choice == '2':
        degrees_to_radians()
    elif user_choice == '3':
        print('\nThank you for using this program.')
        exit()
    else:
        print('\nInvalid option, try again!')
    repeat()

def repeat():
    choice = input("\nPress '1' to use the program again and '2' to exit: ")
    if choice == "1":
        main()
    if choice == "2":
        exit()

def radians_to_degrees():
    radians = int(input('\nEnter an angle in radians: '))
    degrees = radians * 180 / 3.14159
    print('This angle is', degrees, 'degrees.')

def degrees_to_radians():
    degrees = int(input('\nEnter an angle in degrees: '))
    radians = degrees * 3.14159 / 180
    print('This angle is', radians, 'radians.')

main()
