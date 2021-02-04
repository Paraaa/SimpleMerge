from tkinter import * 
from tkinter import filedialog

class GUI():
     
    def __init__(self):
        self.root = Tk()
           
    def buildGUI(self,title,height,width):
    
        size = str(height) + "x" + str(width)
    
        button = Button(self.root, text="Add Files", command = self.browseFiles)
    
        button.grid(row=0,column=0)
    
        self.root.geometry(size)
        self.root.title(title)
        self.root.mainloop()
    

    def browseFiles(self):
        path = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))
        print(path)
        
        
        