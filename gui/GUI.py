from tkinter import * 
from tkinter import filedialog

"""
class to manage gui the gui

"""
class GUI():
    #Termporär zum testen 
    label_set = set()
     
    def __init__(self):
        self.root = Tk()
        self.base_frame = Frame(self.root)
        self.base_frame.pack(side="top", expand=True, fill="both")
       
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
        self.setDynamicFrameObjects()

           
    """
    clear whole frame for next update iteration
    """        
    def clearFrame(self):
        for element in self.base_frame.winfo_children():
            element.destroy()  
         
         
    """
    method to set fixed objects in frame 
    """   
    def setFixedFrameObjects(self):
        actions_frame = Frame(self.base_frame)
        actions_frame.grid(row=0,column=1)
        
        
        
        button = Button(actions_frame, text="Add Files", command = self.browseFiles)
        button.grid(row=0,column=0)   
        
      
    """
    method to set dynamic objects in frame
    """     
    def setDynamicFrameObjects(self):
        
        #Termporär zum testen

        label_Frame = Frame(self.base_frame, bg="black")
        label_Frame.grid(row=0,column=0)
        
        for i,l in enumerate(self.label_set):
            label = Label(label_Frame,text=l)
            label.grid(row=i+1,column=0)
        
        
    """
    method to ope file browser to add file to gui
    """          
    def browseFiles(self):
        path = filedialog.askopenfilenames(initialdir = "/home", 
                                          title = "Select a File", 
                                          filetypes = (("PDF files", 
                                                        "*.pdf*"),))
        #Termporär zum testen
        self.label_set =  self.label_set.union(set(path))
        self.update()