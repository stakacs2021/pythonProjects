#imports
import os
from pathlib import Path
from subprocess import call

def make_txt_file(directory_path, file_name):
    #change given inputted directories and file names to paths
    directory_to_write = Path(directory_path)
    file_to_write = Path(file_name).with_suffix('.txt')

    #check if directory exists if not make it
    directory_to_write.mkdir(parents=True, exist_ok=True)

    #combine file path and file name to make one big one
    file_path = directory_to_write / file_to_write

    #create the file by writing with an empty string
    with open(file_path, 'w') as file:
        file.write(' ')

    print(f"File created successfully: {file_path}")

    return file_path

def open_zed(file_path):
    call(["zed", file_path])


def main():
    #find where we should put the txt file
    directory_path = input("txt file directory path")

    #what should the file be called
    file_name = input("file name")


    open_zed(make_txt_file(directory_path, file_name))



if __name__ == "__main__":
    main()
