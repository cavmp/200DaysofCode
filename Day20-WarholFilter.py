"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg' # Edit this line of code to your images' (folder name/ file name) for the program to work

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    patch = make_recolored_patch(1.5, 0, 1.5)
    patch1 = make_recolored_patch(0, 1.5, 1.5)
    patch2 = make_recolored_patch(1.5, 1.5, 1.5)
    patch3 = make_recolored_patch(2, 2, 0)
    patch4 = make_recolored_patch(0.5, 1, 2)

    image = SimpleImage(PATCH_NAME)
    height = image.height
    width = image.width
    for y in range(height):
        for x in range(width):
            pixel = patch.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel) # makes the first image on top
    for y in range(height):
        for x in range(width):
            pixel = patch1.get_pixel(x, y)
            final_image.set_pixel((width - 1) + (x + 1), y, pixel) # second image on top
    for y in range(height):
        for x in range(width):
            pixel = patch2.get_pixel(x, y)
            final_image.set_pixel(((width * 2) - 2) + (x + 1), y, pixel) # third image on top
    for y in range(height):
        for x in range(width):
            pixel = patch3.get_pixel(x, y)
            final_image.set_pixel(x, (height - 1) + (y + 1), pixel) # duplicates on the left-most bottom
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            final_image.set_pixel((width - 1) + (x + 1), (height - 1) + (y + 1), pixel) # second image on the bottom
    for y in range(height):
        for x in range(width):
            pixel = patch4.get_pixel(x, y)
            final_image.set_pixel(((width * 2) - 2) + (x + 1), (height - 1) + (y + 1), pixel) # third on the bottom
    final_image.show()


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

if __name__ == '__main__':
    main()
