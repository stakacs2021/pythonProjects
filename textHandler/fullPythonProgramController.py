from functools import _make_key
import pdfTxtHandler
import txtHandling



def main():
    #find where we should put the txt file
    directory_path = input("txt file directory path")

    #what should the file be called
    file_name = input("file name")

    txtHandling.make_txt_file(input("tell me pdf file name and tell me directory: "))

    """
    txtHandling.make_txt_file()
    """

    txtHandling.open_zed(directory_path)






if __name__ == "__main__":
    main()
