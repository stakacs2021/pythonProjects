#!/usr/bin/env python3
#this python file creates a program that will intake a txt file path and create a pdf from it
import os
from fpdf import FPDF
#can use pathlib to find cwd for later updates
from pathlib import Path


def txtToPdfConversion(txt_file_path):
    #make the path variable for the txt file and check validity
    txt_path = Path(txt_file_path)
    if not txt_path.is_file():
        print("wrong direct try again")
        return

    #make the fpdf pdf file
    pdf = FPDF()

    #start configuring pdf file
    pdf.add_page()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)

    #open txt_file in read mode and read it all into the new pdf
    with open(txt_path, 'r', encoding='utf8') as open_txt:
        title = open_txt.readline().strip()

        pdf.set_font("Arial", "B", 15)
        pdf.cell(0, 10, title, ln=True, align = 'C')
        pdf.ln(10)

        pdf.set_font("Arial", size = 12)

        page_width = 190
        line_height = 8

        for text in open_txt:
            pdf.multi_cell(page_width, line_height, txt=text.strip(), align='L')

    #now save the pdf to the same directory as infile
    pdf_output_path = txt_path.with_suffix('.pdf')
    pdf.output(str(pdf_output_path))

    print(f"PDF successfully created: {pdf_output_path}")


    return


#def checkSpelling():

#just decided to make it a function to read the file path so I can use this as an example for pdf convert function
#also not using camel case anymore
#testing file
def read_txt_file(txt_file_path):
    #make path object from string pass to func
    txt_path = Path(txt_file_path)

    #check to make sure it is a txt file
    if txt_path.is_file():
        with txt_path.open('r', encoding='utf-8') as file:
            printed_line = file.read()
            print(printed_line)

    else:
        print("Not a valid txt file")




def main():
    #ftaking in input to directory
    txt_file_path = input("file path: ")

    #read_txt_file(txt_file_path)

    #testing new txt to pdfconversion function (works)
    txtToPdfConversion(txt_file_path)





if __name__ == "__main__":
    main()
