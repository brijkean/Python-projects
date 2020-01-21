

from tkinter import *
from tkinter import filedialog
import tkinter as tk
    


class ParentWindow(Frame):  #Frame is the Tkinter class that our class ParentWindow inherits from
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame configuration
        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)

        self.master.title("Select Directory")
        self.master.configure(bg="#F0F0F0")

        gui(self)



def gui(self):
    self.txt1 = tk.Entry(self.master, width=50, text = '')
    self.txt1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(15,0),pady=(43,0), sticky=N+E+W)

    self.btn_browse1 = tk.Button(self.master, width=10, height=1, text='Browse...', command= lambda: selectDir(self))
    self.btn_browse1.grid(row=0, column=0, padx=(25,0), pady=(40,0), sticky=W)
    

def selectDir(self):
    dirname = tk.filedialog.askdirectory()
    self.txt1.delete(0,END)
    self.txt1.insert(0,"{}".format(dirname))
    
    
    
    
    
    


if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
