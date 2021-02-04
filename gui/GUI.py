from tkinter import * 
from tkinter import filedialog
from gui.Presenter import Presenter

"""
class to manage gui the gui
"""
class GUI():
    #Termporär zum testen 
    list_of_pdf = set()
    selected_files = []
     
    def __init__(self):
        self.root = Tk()
        self.presenter= Presenter()
       
    """
    Build first gui instance
    """       
    def buildGUI(self,title,height,width):    
        size = str(height) + "x" + str(width)    
        self.update()            
        self.root.geometry(size)
        self.root.minsize(height,width)  #TODO: Implement resize
        self.root.title(title)
        self.root.mainloop()
    
    """
    update gui 
    """ 
    def update(self):
        self.clearFrame()
        self.setDynamicFrameObjects()
        self.setFixedFrameObjects()

      
    """
    method to set dynamic objects in frame
    """     
    def setDynamicFrameObjects(self):       
        self.box = Listbox(self.root, selectmode='multiple')
        self.box.pack(expand=True,side=LEFT,fill=BOTH)
        self.box.bind('<<ListboxSelect>>',self.addSelected)
    
        for i,content in enumerate(self.list_of_pdf):
            self.box.insert(i,content) 
      
       
    """
    method to set fixed objects in frame 
    """   
    def setFixedFrameObjects(self):  

        button_add_files = Button(self.root, text="Add files", command = self.browseFiles)
        button_add_files.pack(fill=X)
       
        button_merge_files = Button(self.root, text="Merge files", command = self.mergeFiles)
        button_merge_files.pack(fill=X)
        
        self.selected_Items_Label = Label(self.root,text="Selected items")
        self.selected_Items_Label.pack(fill=X)
        
        
    """
    clear whole frame for next update iteration
    """        
    def clearFrame(self):
        for element in self.root.winfo_children():
            element.destroy()  
       
    """
    method to ope file browser to add file to gui
    """          
    def browseFiles(self):
        path = filedialog.askopenfilenames(initialdir = "/home", title = "Select a File", filetypes = (("PDF files",  "*.pdf*"),))
        files_to_add = self.presenter.addFiles(path)     
        self.list_of_pdf =  sorted(set(self.list_of_pdf).union(files_to_add))     
        self.update()
    
    
    
    """
    add selected item to list from listbox
    """
    lastSelectionList = []
    def addSelected(self,event): 
            w = event.widget
            if self.lastSelectionList:
                changedSelection = set(self.lastSelectionList).symmetric_difference(set(w.curselection()))
                self.lastSelectionList = w.curselection()
            else:
                self.lastSelectionList = w.curselection()
                changedSelection = w.curselection()
            
        
            index = int(list(changedSelection)[0])
            value = w.get(index)
        
            if value in self.selected_files:
                self.selected_files.remove(value)
            else:
                self.selected_files.append(value)
            print("Selected items", self.selected_files)
            self.selected_Items_Label['text'] = "\n".join(self.selected_files)

    """
    merge selected files from view 
    """   
    def mergeFiles(self):    
        if len(self.selected_files) > 1: 
            self.presenter.mergeFiles(self.selected_files)
        else:
            print("To merge files select more than one file")
    
    
    
        