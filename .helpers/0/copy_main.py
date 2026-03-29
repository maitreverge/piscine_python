import os
import shutil

MAIN_FILE = "./main.py"
EXCLUDED_DIRS = {"__pycache__", ".mypy_cache", "mypy_cache"}

def main():
    """
    Copy the `main.py` in all subfolders.
    """
    for root, dirs, _ in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for dir_name in dirs:
            dst = os.path.join(root, dir_name, "main.py")
            shutil.copy2(MAIN_FILE, dst)

main()