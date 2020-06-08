from PIL import Image, ImageChops
from re import search
from sys import argv, exit
from os import getcwd
from os.path import isfile
from re import search
import PySimpleGUI as sg

def are_images_equal(img1, img2):
    return ImageChops.difference(img1, img2).getbbox() is None

def is_image(file_name):
    return search(r'^(.*)\.(JPEG|JPG|PNG)$', file_name) != None

def exit_error(error_message):
    print('usage: python find_duplicate_images.py <img1> <img2>')
    print(error_message)
    exit()

if len(argv) != 3:
    exit_error('Wrong number of arguments given.')

if not isfile(argv[1]) or not is_image(argv[1]):
    exit_error('First argument is not a valid image.')

if not isfile(argv[2]) or not is_image(argv[2]):
    exit_error('Second argument is not a valid image.')

img1_path = argv[1]
img2_path = argv[2]
img1 = Image.open(img1_path)
img2 = Image.open(img2_path)

if img1.format != 'JPEG' or img1.format != 'GIF':
    img1_converted = img1.convert('RGB')
    img1_filename = search(r'([A-Za-z0-9]+\.JPG|JPEG$)', img1_path).group()
    img1_path = f'{getcwd()}/.tmp_{img1_filename}.PNG'
    print(argv[1])
    print(img1_path)
    img1_converted.save(img1_path)

if img2.format != 'JPEG' or img2.format != 'GIF':
    img2_converted = img2.convert('RGB')
    img2_filename = search('[A-Za-z0-9]+\.JPG|JPEG$', img2_path).group()
    img2_path = f'{getcwd()}/.tmp_{img2_filename}.PNG'
    img2_converted.save(img2_path)

if are_images_equal(img1, img2):
    print('Images are same.')
else:
    print('Images are different.')


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Duplicate found!')],
            [sg.Image(img1_path, size=(500, 500)), sg.Image(img2_path, size=(500, 500))],
            [sg.Button('Keep 1'), sg.Button('Keep 2')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    print('You selected: ', event)

window.close()
