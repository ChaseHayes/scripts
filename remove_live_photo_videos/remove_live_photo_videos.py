from sys import argv, exit
from os import listdir, remove
from os.path import isdir
from re import match

def exit_error(error_message):
    print 'usage: remove_live_photo_videos.py <dir>'
    print error_message
    exit()

def is_image(file_name):
    return match(r'^(.*)\.(JPEG|JPG|PNG)$', file_name) != None

def is_video(file_name):
    return match(r'^(.*)\.(MOV)$', file_name) != None

def get_file_no_extension(file_name):
    return match(r'^(.*)\.(JPEG|JPG|PNG|MOV)', file_name).group(1)
 
def is_video_for_image(image_file_name, video_file):
    return match(r'^{0}\.MOV$'.format(image_file_name), video_file) != None

def get_live_photo_video(file_name, video_files):
    get_file_no_extension(file_name)
    matched_files = filter(lambda video_file: is_video_for_image(get_file_no_extension(file_name), video_file), video_files)
    return matched_files[0] if len(matched_files) > 0 else None
    
if len(argv) != 2:
    exit_error('missing <dir> argument')

if isdir(argv[1]) != True:
    exit_error('argument <dir> not a directory')

dir_path = argv[1]
print 'This argument is a directory: {0}'.format(dir_path)

dir_files = listdir(dir_path)
image_files = sorted(filter(lambda file: is_image(file), dir_files))
video_files = filter(lambda file: is_video(file), dir_files)

print 'Here\'s all of the live photo videos I found:'
for image_file in image_files:
    video_file = get_live_photo_video(image_file, video_files)
    if video_file != None:
        full_video_path = '{0}/{1}'.format(dir_path, video_file)
        print 'Video path: {0}'.format(full_video_path)
        remove(full_video_path) 
        print 'Removed video path'
print 'Done'
