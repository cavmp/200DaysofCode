"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use 
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    # Create new image to contain mirror reflection vertically
    mirror = SimpleImage.blank(width, height * 2)

    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel(x, (height * 2) - (y + 1), pixel)
    return mirror


def main():
    """
    This program tests your make_reflected function by displaying
    the original image of the mountain as well as the resulting image
    from your make_reflected function.
    """
    original = SimpleImage('images/mt-rainier.jpg') # For this line of code, edit yours with regards to ('the folder of the file/ filename')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg') # Do the same for this one. The code won't work if this line of code is not edited as you don't have this exact folder and picture
    reflected.show()

if __name__ == '__main__':
    main()
