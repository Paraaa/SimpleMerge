
from PyPDF2 import PdfFileMerger, PdfFileReader


class PDF:

    def __init__(self):
        pass

    """
    merge files with PyPDF2 and write it to destination location
    """

    def merge(self, files, path):
        merger = PdfFileMerger()
        for pdf_file_path in files:
            pdf_file = open(pdf_file_path, "rb")
            pdf = PdfFileReader(pdf_file)
            merger.append(pdf)
        merger.write(path)
