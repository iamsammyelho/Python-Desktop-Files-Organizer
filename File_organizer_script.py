import os
import shutil as st
import sys
import time

#  FIle extensions format
audio = (".mp3", ".wav", ".wma", "m4a")
video = (".mp4", ".mkv", "mpeg")
pdf = (".pdf", ".pdf")
picture = (".jpeg", ".png", ".jpg", ".gif")


# function for getting files
def get_files(folder_path, *ext):
    path = []
    file_list = []
    # Searching through the "folder_path
    for items in os.walk(folder_path):
        path.append(items)
    # Indexing out directories and returning files only
    directory = path[0]
    files = directory[2]
    for items in files:
        for i in ext:
            if i in items:
                try:
                    #  adding files to the file list
                    file_list.append(items)
                except FileNotFoundError:
                    pass
    # checks if file list is not empty
    if file_list:
        return file_list
    else:
        # ending the program
        sys.exit()


# function for moving the file
def move_files(folder, destination, ext):
    files = get_files(folder, *ext)
    move_to = folder + "\\" + destination
    path_x = []
    for items in files:
        # joining the movies and the root for create a path
        path = folder + "\\" + items
        #  filtering out double copies
        if path not in path_x:
            path_x.append(path)
        elif path in path_x:
            continue
    try:
        # creating a folder
        os.mkdir(move_to)
        # moving files
        time.sleep(2)
        for items in path_x:
            st.move(items, move_to)
            time.sleep(0.2)
    except FileExistsError:
        try:
            for items in path_x:
                st.move(items, move_to)
                time.sleep(0.2)
        except OSError:
            for items in path_x:
                os.remove(items)
                time.sleep(1)
            print("deleting copies.....")


# moves_files(from path, to folder(creates folder in same path if it does not exist), extension(files type to move))
# File type parameters takes audio, video or pdf
move_files(r'C:\Users\pc\Desktop', "Pictures", picture)
sys.exit()
# TIPS for improvements
# Capture the part where if there is only one file type in the directory, the code will still work
# Capture a part where the user can decide to check all directories in a root for filees and copy them
