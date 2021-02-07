from tkinter import * 
from tkinter import filedialog,messagebox
from gui.Presenter import Presenter

"""
class to manage gui the gui
"""
class GUI():
    """
    construct
    """ 
    def __init__(self):
        self.root = Tk()
        self.presenter= Presenter()
        self.mergeBox = None
        self.box = None
        self.list_of_pdf = set()
        self.selected_files = []
            
    """
    Build first gui instance
    """       
    def buildGUI(self,title,height,width):    
        size = str(height) + "x" + str(width)    
        self.update()            
        self.root.geometry(size)
        self.root.minsize(height,width)  
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=1)
        self.root.rowconfigure(1,weight=2)
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
        label_listbox = Label(self.root,text='Imported files')   
        label_listbox.grid(row=0,column=0,sticky='nsew')
        
        self.box = Listbox(self.root, selectmode='multiple')
        self.box.grid(row=1,column=0,sticky='nsew')
        self.box.unbind('<<ListboxSelect>>')
    
        for i,content in enumerate(self.list_of_pdf):
            self.box.insert(i,content) 
      
       
    """
    method to set fixed objects in frame 
    """   
    def setFixedFrameObjects(self):  
        menubar = Menu(self.root)
        files = Menu(menubar,tearoff=0)
        files.add_command(label='Add files', command=self.browseFiles)
        
        edit_on_files = Menu(menubar,tearoff=0)
        edit_on_files.add_command(label='Merge files', command=self.openMergeView)
        
        menubar.add_cascade(menu=files, label='File')
        menubar.add_cascade(menu=edit_on_files,label='Edit')
        
        self.root.config(menu=menubar)
        
    """
    clear whole frame for next update iteration
    """        
    def clearFrame(self):
        for element in self.root.winfo_children():
            element.destroy()  
        self.lastSelectionList =  []
        self.selected_files = []
        
        
    """
    method to open file browser to add file to gui
    """          
    def browseFiles(self):
        path = filedialog.askopenfilenames(initialdir = "/home", title = "Select a File", filetypes = (("PDF files",  "*.pdf*"),))
        files_to_add = self.presenter.addFiles(path)     
        self.list_of_pdf =  sorted(set(self.list_of_pdf).union(files_to_add))     
        self.update()
    
    
    """
    method to set path to save file to
    TODO: So schreiben, dass andere funktionen diese Methode auch nutzen können
    """
    def saveAs(self):
        if len(self.selected_files) > 1: 
            selected_path = filedialog.asksaveasfile(mode='w',defaultextension=".pdf").name
            if selected_path is None:
                return
            self.mergeFiles(selected_path)
        else:
            messagebox.showinfo(title=None,message="You need atleast two files to merge files.")
      
    
    """
    select all items in the added items list
    """
    def selectAll(self):
        self.selected_files = list(self.list_of_pdf)
        self.mergeBox.delete(0,END)
        for item in self.selected_files:
            self.mergeBox.insert(END,item)
        self.box.select_set(0,END)

        
    
    """
    deselect all items in the added items list
    """
    def deselectAll(self):
        self.selected_files = []
        self.mergeBox.delete(0,END)
        self.box.selection_clear(0,END)
   
    """
    add selected item to list from listbox
    """
    lastSelectionList = []
    def addSelected(self,event): 
            w = event.widget
            if w.size() > 0:
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
                    #Remove item if uses dont want to merge the file anymore
                    self.mergeBox.delete(self.mergeBox.get(0,END).index(value))
                else:
                    self.selected_files.append(value)
                    #Add file to view 
                    self.mergeBox.insert(END,value)
   
   
    """
    Open a merge view to select pdf files to merge
    """    
    def openMergeView(self):
        self.update()
        self.box.bind('<<ListboxSelect>>', self.addSelected)
        self.box.select_clear(0,END)
        
        label = Label(self.root,text="Files to merge")
        label.grid(row=0,column=1,sticky='nsew')
        
        self.mergeBox = Listbox(self.root,selectmode='single')
        self.mergeBox.grid(row=1,column=1,sticky='nsew')

        action_frame = Frame(self.root)
        action_frame.grid(row=1,column=2,sticky='nsew')
             
        button_merge = Button(action_frame, text="Save as", command = self.saveAs)
        button_merge.grid(row=2,column=0,sticky='new')
    
        button_select_all = Button(action_frame, text="Select all", command = self.selectAll)
        button_select_all.grid(row=4,column=0,sticky='new')
        
        button_select_all = Button(action_frame, text="Deselect all", command = self.deselectAll)
        button_select_all.grid(row=5,column=0,sticky='new')
                
        button_close = Button(action_frame, text="Close", command = self.update)
        button_close.grid(row=6,column=0,sticky='new')
        

    """
    merge selected files from view 
    """   
    def mergeFiles(self,path):    
        self.presenter.mergeFiles(self.selected_files,path)
    
    
    
    
        