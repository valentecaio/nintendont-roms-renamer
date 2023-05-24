#!/usr/bin/python3

import os

TEST     = True     # set to True to test the script without modifying files
UNDO     = False    # set to True to undo the renaming
GAMESDIR = "games/" # directory containing the games to rename

# strings to replace in the filenames in the function preprocess_filenames()
# the key is the string to replace, the value is the string to replace it with
# example: "Disc 1" will be replaced with "disc1"
disc_strings = {"disc1": ["(Disc 1)", "DVD 1"], "disc2": ["(Disc 2)", "DVD 2"]}
def preprocess_filenames():
    for filename in os.listdir():
        new_filename = filename
        for disc, disc_strings_list in disc_strings.items():
            for disc_string in disc_strings_list:
                if disc_string in new_filename:
                    new_filename = new_filename.replace(disc_string, disc)
        if new_filename != filename:
            print(f'Renaming "{filename}" to "{new_filename}"')
            if not TEST: os.rename(filename, new_filename)


def rename_to_nintendont_format():
    for filename in sorted(os.listdir()):
        if os.path.isfile(filename):
            old_name, extension = os.path.splitext(filename)

            if "disc1" in old_name:
                new_name = "game" + extension
                subdirname = old_name.replace(" disc1", "")
            elif "disc2" in old_name:
                new_name = "disc2" + extension
                subdirname = old_name.replace(" disc2", "")
            else:
                new_name = "game" + extension
                subdirname = old_name

            # rename file
            print(f'Renaming "{filename}" to "{new_name}"')
            if not TEST: os.rename(filename, new_name)

            # create the subfolder if it doesn't exist
            if not os.path.exists(subdirname):
                print(f'Creating folder "{subdirname}"')
                if not TEST: os.mkdir(subdirname)                

            # move file into the subfolder
            print(f'Moving "{new_name}" into folder "{subdirname}"\n')
            if not TEST: os.rename(new_name, os.path.join(subdirname, new_name))

def undo_renaming():
    # get the list of subdirectories in the current directory
    subdirectories = [name for name in sorted(os.listdir()) if os.path.isdir(name)]

    for subdir in subdirectories:
        print()
        files = os.listdir(subdir)

        for filename in files:
            old_name, extension = os.path.splitext(filename)

            if old_name == "game":
                new_name = subdir + extension
            else:
                new_name = subdir + " disc2" + extension

            # move the file out of the subfolder
            old_name = os.path.join(subdir, filename)
            print(f'Moving "{old_name}" to "{new_name}"')
            if not TEST: os.rename(old_name, new_name)

        # remove the subfolder if it's empty
        if not os.listdir(subdir):
            print(f'Removing empty folder "{subdir}"')
            if not TEST: os.rmdir(subdir)


if __name__ == "__main__":
    os.chdir(GAMESDIR)

    print("Script parameters:")
    print(f'  TEST = {TEST}')
    print(f'  UNDO = {UNDO}')
    print(f'  GAMESDIR = "{GAMESDIR}"\n')

    print("This script will rename the files in the GAMESDIR directory to the Nintendont format.")
    print("It will **NOT** change any file or directory if the TEST parameter is set to True.")
    print("You can undo the renaming by running the script with the UNDO parameter set to True.\n")

    if not TEST:
        print("WARNING: \nRUNNING THE SCRIPT WILL MODIFY FILES AND FOLDERS IN THE GAMESDIR DIRECTORY.")
        print("MAKE SURE YOU HAVE A BACKUP OF THE FILES BEFORE PROCEEDING.")
    else:
        print("You are running the script in test mode. No files will be modified.")
        print("If you want to modify files, edit the TEST parameter in the script.")
    input("\nPress any key to proceed or close the window to cancel.")

    if UNDO:
        print("---- UNDOING RENAMING ----")
        undo_renaming()
    else:
        print("---- PREPROCESSING FILENAMES ----")
        preprocess_filenames()
        print("\n\n---- RENAMING TO NINTENDONT FORMAT ----")
        rename_to_nintendont_format()

    print("\n---- FINISHED ----")
    input("Press Enter to close.")

