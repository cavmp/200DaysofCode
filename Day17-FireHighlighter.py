from simpleimage import SimpleImage

DEFAULT_FILE = 'images/greenland-fire.png'

def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3 # This will be the standard for 'sufficiently red' pixels
        if pixel.red >= average:
            # This will make the pixels entirely red
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        pixel.blue = average
        pixel.green = average
        if pixel.red != 255:
            pixel.red = average
    return image

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()


    
def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
