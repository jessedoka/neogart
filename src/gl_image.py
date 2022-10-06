import PIL.Image
from argparse import ArgumentParser
from github.identicon import Identicon
from random import randint

GIT_LEVELS = ["0", "1", "2", "3", "4" ]
# 0, 3, 8, 10, 13

def resize_image(image):
    # convert image into 7x7 size
    resized_image = image.resize((7, 7))
    return resized_image

def grayify(image):
    # convert image to grayscale
    gray_image = image.convert("L")
    return gray_image
    
def convert_to_gl(image):
    pixels = image.getdata()
    characters = "".join([GIT_LEVELS[pixel//52] for pixel in pixels])
    return characters

def identicon(new_width=7):
    identicon = Identicon.from_identifier(randint(0, 480938))
    image = identicon.generate_image()  # requires PIL
    new_image_data = convert_to_gl(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    gl_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    return gl_image


    


if __name__ == '__main__':
    print(identicon())

