
import sys

import argparse 
import re
from PyPDF2 import PdfFileReader, PdfFileMerger
from os import listdir
from os.path import isfile, join



def print_PDF_information(source):
    pdf = open(source, 'rb')
    reader = PdfFileReader(pdf)
    information = reader.getDocumentInfo()
    number_of_pages = reader.getNumPages()
    isEncrypted = reader.isEncrypted
    print_dict(information)      
    print("Encrypted: ", isEncrypted)
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
     
     
     
#TODO: Check if file is a pdf.
def concaternate_pdf_files_in_folder(source, name='document.pdf',passwort=None):
    merger = PdfFileMerger()
    
    files = [f for f in listdir(source) if isfile(join(source, f))]
    #print(files)



    for i in range(len(files)):
        file_to_merge = open(source+'/'+files[i], 'rb')
        pdf = PdfFileReader(file_to_merge)
        if passwort is not None:
            pdf.decrypt(passwort)
    
        merger.append(pdf)
    
    merger.write(name)
    

     

if __name__ == "__main__":
    #print_PDF_information("/home/andrejschwanke/Dokumente/python_scripts/pdfpy/Anwendungen_der_KI_Gruppe3.pdf")
    #print_PDF_information("/home/andrejschwanke/Dokumente/python_scripts/pdfpy/07_Patientensicherheit_Medizinprodukt.pdf")
    concaternate_pdf_files_in_folder('/home/andrejschwanke/Dokumente/python_scripts/pdfpy/pdfFolien',name='file.pdf')
     



