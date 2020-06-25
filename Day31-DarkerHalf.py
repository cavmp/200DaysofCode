"""
File: darkerhalf.py
-------------------
This program makes the right-side half of any uploaded image darker.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'


def main():
    # Get file and load image
    filename = get_file()
    original = SimpleImage(filename)

    # Show the image before the transform
    original.show()

    # Apply the filter
    image = darker_half(filename)

    # Show the image after the transform
    image.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def darker_half(filename):
    image = SimpleImage(filename)
    for pixel in image:
        # if pixel is in right half of image
        # (e.g. width is 100, right half begins at x=50)
        if pixel.x >= image.width // 2:
            pixel.red *= 0.5
            pixel.green *= 0.5
            pixel.blue *= 0.5
    return image

if __name__ == '__main__':
    main()
