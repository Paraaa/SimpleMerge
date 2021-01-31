
import sys
import os
import argparse 
import re
from PyPDF2 import PdfFileReader




def print_PDF_information(source):
    pdf = open(source, 'rb')
    reader = PdfFileReader(pdf)
    information = reader.getDocumentInfo()
    number_of_pages = reader.getNumPages()
    print_dict(information)      
    print("Number of pages: ",number_of_pages)


def removeChar(charToRemove, text):
    cleared_Text = re.sub('['+charToRemove+']', '', text)
    return cleared_Text

def print_dict(dict):
    for key, value in dict.items():
        key_print = removeChar('/',key)        
        if value == '':
            print(key_print,": ", "None")
        else:
            value_print = removeChar('/',value)
            print(key_print, ": ", value_print) 
     
     

if __name__ == "__main__":
    print_PDF_information("/home/andrejschwanke/Dokumente/python_scripts/pdfpy/Anwendungen_der_KI_Gruppe3.pdf")
     
     



