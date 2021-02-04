from tkinter import * 
from tkinter import filedialog

"""
class to manage gui the gui
"""
class GUI():
     
    label_list = []
     
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack(side="top", expand=True, fill="both")
       
    """
    Build first gui instance
    """       
    def buildGUI(self,title,height,width):    
        size = str(height) + "x" + str(width)    
        self.update()    
        self.root.geometry(size)
        self.root.title(title)
        self.root.mainloop()
    
    """
    update gui 
    """ 
    def update(self):
        self.clearFrame()
        self.setFixedFrameObjects()
        
        #label
        for i,l in enumerate(self.label_list):
            label = Label(self.frame,text=l)
            label.grid(row=i+1,column=0)
       
    """
    clear whole frame for next update iteration
    """        
    def clearFrame(self):
        for element in self.frame.winfo_children():
            element.destroy()  
         
         
    """
    method to set fixed objects in frame 
    """   
    def setFixedFrameObjects(self):
        button = Button(self.frame, text="Add Files", command = self.browseFiles)
        button.grid(row=0,column=0)   
        
      
    """
    method to set dynamic objects in frame
    """     
    def setDynamicFrameObjects(self):
        pass 
        
        
    """
    method to ope file browser to add file to gui
    """          
    def browseFiles(self):
        path = filedialog.askopenfilename(initialdir = "/home", 
                                          title = "Select a File", 
                                          filetypes = (("PDF files", 
                                                        "*.pdf*"),))
        self.label_list.append(path)
        self.update()