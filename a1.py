# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME Sergio Alcazar
# EMAIL smalcaza@uci.edu
# STUDENT ID 73371481

import shlex
from pathlib import Path 

def create_file(path_str, name):
    directory = Path(path_str)
    if not directory.exists() or not directory.is_dir():
        print("ERROR")
        return
    new_file = directory / (name + ".dsu")
    if new_file.exists():
        print("ERROR")
        return
    new_file.touch()
    print(new_file)

def delete_file(path_str):
    target = Path(path_str)
    if not target.exists() or target.suffix != ".dsu":
        print("ERROR")
        return
    print(f"{target} DELETED")
    target.unlink()

def read_file(path_str):
    target = Path(path_str)
    if not target.exists() or target.suffix != ".dsu":
        print("ERROR")
        return
    with target.open() as f:
        contents = f.read()
    if contents.strip() == "":
        print("EMPTY")
    else:
        print(contents)

def run():
    pass

if __name__ == "__main__":
    run()
