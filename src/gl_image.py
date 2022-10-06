import PIL.Image
from argparse import ArgumentParser


GIT_LEVELS = ["0", "1", "2", "3", "4" ]
# 0, 3, 8, 10, 13

def resize_image(image):
    # convert image into 52x7 size
    resized_image = image.resize((52, 7))
    return resized_image

def grayify(image):
    # convert image to grayscale
    gray_image = image.convert("L")
    return gray_image
    
def convert_to_gl(image):
    pixels = image.getdata()
    characters = "".join([GIT_LEVELS[pixel//51] for pixel in pixels])
    return characters

def main(path, new_width=52):
    # ascii characters used to build the output text


    # read image
    try:
        img = PIL.Image.open(path)
    except:
        print(path, "is not valid")

    new_image_data = convert_to_gl(grayify(resize_image(img)))

    pixel_count = len(new_image_data)
    gl_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    print(gl_image)

    with open("gl_image.txt", "w") as f:
        f.write(gl_image)



if __name__ == '__main__':
    # image file as command line argument
    parser = ArgumentParser(description="Convert an image to a git level image")
    parser.add_argument("path", help="The path to the image file")
    args = parser.parse_args()

    main(path=args.path)

