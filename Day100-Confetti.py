import turtle
import random

numberOfConfetti = 200

colors = ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond',
          'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
          'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkkhaki',
          'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen',
          'darkslateblue', 'darkslategray', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray',
          'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold',
          'goldenrod', 'gray', 'green', 'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki',
          'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan',
          'lightgoldenrodyellow', 'lightgreen', 'lightgray', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue',
          'lightslategray', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon',
          'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue',
          'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin',
          'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod',
          'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue',
          'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna',
          'silver', 'skyblue', 'slateblue', 'slategray', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle',
          'tomato', 'turquoise', 'violet', 'white', 'whitesmoke', 'yellow', 'yellowgreen']

num = random.randrange(len(colors))

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
window = turtle.Screen()
window.bgcolor("#ffffff")

myPen.pensize(1)
radius = 9  # Radius of a confetti, in pixels
list = []

def addText(x, y, text, color, size):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.color(color)
    myPen.write(text, None, align="center", font=("Times", size, "normal"))

# Add Confetti
for confetti in range(0, numberOfConfetti):
    overlap = True
    while overlap:
        x = random.randint(-180 + radius, 180 - radius)
        y = random.randint(-180 + radius, 180 - radius)
        # Check if new confetti overlap with any existing confetti
        overlap = False
        for confetti in list:
            # Use Pythagoras Formula to calculate the distance between two confetti
            distance = ((confetti[0] - x) ** 2 + (confetti[1] - y) ** 2) ** 0.5
            # If two confetti are too close to each other, then they will overlap!
            if distance <= (2 * radius) + 2:
                overlap = True

    list.append([x, y])

    addText(0, 40, "HAPPY", 'black', "45")
    addText(0, 0, "100 DAYS", 'purple', "45")
    addText(0, -40, "OF CODING!", 'black', "45")

    # Generate a random colour!
    num = random.randrange(0, len(colors), 1)
    myPen.penup()
    myPen.goto(x, y - radius)
    myPen.pendown()
    myPen.fillcolor(colors[num])
    myPen.color(colors[num])
    myPen.begin_fill()
    myPen.circle(radius - 2)
    myPen.end_fill()
    print(str(len(list)) + " confetti")
