import os
import shutil
import getpass

def clearDirectory(directory):
    files = os.listdir(directory)
    for file in files:
        filepath = os.path.join(directory, file)
        try:
            if os.path.isfile(filepath):
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        except Exception as e:
            print(e)
        finally:
            exit()

username = getpass.getuser()
option = int(input(
    "Which temp folder should be cleared ? \n1 - Appdata \n2 - Windows \n0 - Quit \n"))

match option:
    case 1:
        clearDirectory(f"C:\\Users\\{username}\\AppData\\Local\\Temp")
    case 2:
        clearDirectory(f"C:\\Windows\\Temp")
    case 0:
        exit()