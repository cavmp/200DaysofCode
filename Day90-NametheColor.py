def main():
    color_name = input("Type the name of a colour (Type 'exit' when done using this program): ").lower()
    color_code = ""

    file = open("colors", "r")

    for line in file:
        colour = line.split(",")
        if color_name == colour[0].lower():
            color_code = colour[1]

    # Output:
    if color_code == "":
        print("We could not find your colour.\n")
    else:
        print(color_code)

    if color_name == "exit":
        exit()
    else:
        main() # repeats

    # Let's close the file
    file.close()



if __name__ == "__main__":
    main()
