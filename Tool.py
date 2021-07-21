import os
import shutil

# ============================= # your directories there
game_dir = ''
back_dir = ''  # write only the name, not the entire path
# ============================= # please make sure there are no backup files named "save00" or "li-show"


# don't change anything below this line unless you know what you are doing

back_dir = os.path.join(game_dir, back_dir)
forbidden = ['save00', 'li-show']  # names that have a particular role

if game_dir == '' or not os.path.exists(game_dir):
    print("Game directory is not set / existing. Please change it in the code\n"
          "If you don't know how to do that: \n"
          "Select the python file and right click it. Then select \"Edit with IDE\" and pick the latest one\n"
          "Get the correct directory path of the game (be careful) as a string and copy it after \"game_dir = \"\n"
          "Then replace every \\ with a /\n"
          "Remember that the name must be between \"\" or \'\'\n"
          "Save and exit the file, and then try to launch it again")
    while True:
        input()

if not os.path.exists(back_dir):
    try:
        os.makedirs(back_dir)
        print(f"No backup directories with the name \"{back_dir.split('/')[-1]}\" were found, so one was created")
    except:
        print('Something went wrong, check the directories again. Be comprehensive, this app is an experiment')
    while True:
        input()


def show():
    files = os.listdir(back_dir)
    if len(files) != 0:
        for n, file in enumerate(sorted(files)):
            print(f"{n + 1}: {file}")
    else:
        print("Backup directory is empty\n")


def help_():
    print("\n\nAvailable functions (not cap sensitive):\n"
          "help: this dialogue\n"
          "show: displays the name of all files in the backup directory\n"
          "settings: shows the directories used by this program. To modify them you have to edit the code\n"
          "\nAvailable functions (cap sensitive):\n"
          "save + file name: saves the current save file with the given name \n"
          "load + file name: loads the backup file with the given name, deleting the current save file \n"
          "delete + file name: delete the backup file with the given name\n\n")


def settings():
    print(f"\nGame directory: {game_dir}\n"
          f"Backup directory: {back_dir}\n")


def delete(file_name):
    while not os.path.exists(os.path.join(back_dir, file_name)):
        print(f"No file named \"{file_name}\" was found")
        choice = input(
            "Do you want do delete another file? Type \"li-show\" to see available files and continue: ").lower()
        if choice in ['y', 'yes', 'li-show']:
            if choice == 'li-show':
                show()
            file_name = input("File to delete: ")
        else:
            return

    print('Please wait...')
    shutil.rmtree(os.path.join(back_dir, file_name))
    print(f'The backup file named \"{file_name}\" was deleted')


def save(file_name):
    while os.path.exists(os.path.join(back_dir, file_name)) or file_name in forbidden:
        if file_name in forbidden:
            print(f"You can't name the file like that")
            file_name = input("New name for the backup file: ")
        else:
            print(f"A file with the name \"{file_name}\" already exists")
            choice = input("Do you want to replace it? If not, write a new name for the new file: ")
            if choice.lower() not in ['y', 'yes']:
                file_name = choice
            else:
                shutil.rmtree(os.path.join(back_dir, file_name))
                print('Previous backup file deleted')
                break

    print("Please wait...")
    shutil.copytree(os.path.join(game_dir, 'save00'), os.path.join(os.path.join(back_dir, file_name)))
    print(f"Backup file created: \"{file_name}\"\n\n")


def load(file_name):
    while not os.path.exists(os.path.join(back_dir, file_name)) or file_name in forbidden:
        if file_name in forbidden:
            print(f'This is not an allowed file name. Please rename an eventual backup file with this name')
        else:
            print(f"A backup file named \"{file_name}\" was not found")

        file_name = input("Input the name of an existing file or type \"li-show\" to see available files: ")

        if file_name.lower() == 'li-show':
            show()
            file_name = input("\nInput the name of an existing file: ")

    print("Please wait...")
    shutil.rmtree(os.path.join(game_dir, 'save00'))
    shutil.copytree(os.path.join(back_dir, file_name), os.path.join(game_dir, 'save00'))
    print(f'File \"{file_name}\" loaded with success\n\n')


while True:
    check = False
    while not check:
        command = input("What do you want to do?: ")
        if command in ['help', 'Help']:
            help_()
        elif command in ['settings', 'Settings']:
            settings()
        elif command in ['show', 'Show']:
            show()
        else:
            try:
                func, f_name = command.split(' ')
                func, f_name = func.strip(), f_name.strip()
                check = True
            except ValueError:
                print("The given command can't be interpreted. Make sure it is written correctly or type \"help\"")

    if func.lower() == 'load':
        load(f_name)
    elif func.lower() == 'save':
        save(f_name)
    elif func.lower() == 'delete':
        delete(f_name)
    elif func.lower() == 'help':
        print("The \"help\" function does not require a two words command")
        help_()
    else:
        print(f"There is no function with the name \"{func}\". Type \"help\" so see available functions\n")
