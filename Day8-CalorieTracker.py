def calorie_log():

    track_calories = {}                   # Create empty food list

    while True:
        food = input("What did you eat today?: ")
        if food == "":
            break
        serving_size = float(input("Serving Size: "))
        calories = float(input("Calories per Serving: "))
        total_calories = serving_size * calories # Computes the total calories with regards to service size and calories
        track_calories[food] = total_calories
        print(food, "->", track_calories[food]) # Prints the total calories of the food

    return track_calories

def print_calorie_log(track_calories):
    print("This is everything you ate today:")
    for food in track_calories:
        print(food, "->", track_calories[food], "calories") # Prints the total calories of all food consumed

    count = 0
    for food in track_calories:
        count += track_calories[food] # Adds the total calories of all food consumed
    print("You consumed", str(count), "calories today.")


def main():
    log = calorie_log()
    print_calorie_log(log)

if __name__ == '__main__':
    main()
