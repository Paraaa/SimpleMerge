
import re
from os.path import expanduser
from PyPDF2 import PdfFileMerger,PdfFileReader,PdfFileWriter


class PDFModifier:
    
    def __init__(self):
        pass

    
    def merge(self,files,filename,path=expanduser("~")):
        merger = PdfFileMerger()
        
        for pdf_file_path in files:
            pdf_file = open(pdf_file_path,"rb")
            pdf = PdfFileReader(pdf_file)
            merger.append(pdf)
            

        merger.write(path + "/" + self.checkFileName(filename))
   
       
    def checkFileName(self,filename):
        regex = "([^\\s]+(\\.(?i)(pdf))$)"
        if filename:
            print(filename)
            regex_check = re.compile(regex)
            if(re.search(regex_check,filename)):
                return filename
            else:
                return filename + ".pdf"
        else: 
            return "document.pdf"