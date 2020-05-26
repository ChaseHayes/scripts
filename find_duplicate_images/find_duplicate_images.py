from PIL import Image, ImageChops
from re import match
from sys import argv, exit
from os.path import isfile

def are_images_equal(img1, img2):
    return ImageChops.difference(img1, img2).getbbox() is None

def is_image(file_name):
    return match(r'^(.*)\.(JPEG|JPG|PNG)$', file_name) != None

def exit_error(error_message):
    print 'usage: python find_duplicate_images.py <img1> <img2>'
    print error_message
    exit()

if len(argv) != 3:
    exit_error('Wrong number of arguments given.')

if not isfile(argv[1]) or not is_image(argv[1]):
    exit_error('First argument is not a valid image.')

if not isfile(argv[2]) or not is_image(argv[2]):
    exit_error('Second argument is not a valid image.')

img1 = Image.open(argv[1])
img2 = Image.open(argv[2])

if are_images_equal(img1, img2):
    print 'Images are same.'
else:
    print 'Images are different.'
