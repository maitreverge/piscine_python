import os
import shutil

def os_walk():
    for root, dirs, files in os.walk('.'):
        print("Current directory:", root)
        print("Subdirectories:", dirs)
        print("Files:", files)

MAIN_FILE = "./main.py"
def main():
    # os_walk()

    for _, dirs, _ in os.walk('.'):
        for dir_name in dirs:
            shutil.copy2(MAIN_FILE, os.path.join(dir_name, "main.py"))

main()