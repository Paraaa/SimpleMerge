import ntpath

from PDF.PDFModifier import PDFModifier

"""
Manage actions from the gui
"""
class Presenter:
    
    file_to_path_dict = {}
    
    
    def __init__(self):
        self.pdfModifier = PDFModifier()  
    
    """
    Add files to local dictonary and split them into simple name an path
    @return: Returns the file names as a simple names as a set
    """
    def addFiles(self,path_list): 
        simple_file_name_list = []
       
        for path in path_list: 
            simple_file_name = ntpath.basename(path)
            simple_file_name_list.append(simple_file_name)
            self.file_to_path_dict[simple_file_name] = path
        
        return set(simple_file_name_list)
    
    
    """
    call PDFModifier to set merge requested files
    """
    def mergeFiles(self,files_to_merge,filename,path_to_save_to):       
        paths_of_files = [] 
        for file in files_to_merge:
            paths_of_files.append(self.file_to_path_dict.get(file))
      
        self.pdfModifier.merge(paths_of_files,filename,path=path_to_save_to)
        
        
    
            
             