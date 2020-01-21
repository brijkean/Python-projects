

from tkinter import *
import tkinter as tk
    


class ParentWindow(Frame):  #Frame is the Tkinter class that our class ParentWindow inherits from
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame configuration
        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)

        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        gui(self)



def gui(self):
    self.txt1 = tk.Entry(self.master, width=50, text = '')
    self.txt1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(30,0),pady=(43,0),sticky=N+E+W)
    self.txt2 = tk.Entry(self.master, width=50, text = '')
    self.txt2.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(30,0),pady=(13,0),sticky=N+E+W)

    self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...')
    self.btn_browse1.grid(row=0, column=0, padx=(25,0), pady=(40,0), sticky=W)
    self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...')
    self.btn_browse2.grid(row=1, column=0, padx=(25,0), pady=(10,0), sticky=W)

    self.btn_check = tk.Button(self.master, width=12, height=2, text='Check for files...')
    self.btn_check.grid(row=3, column=0, padx=(25,0), pady=(10,10), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program')
    self.btn_close.grid(row=3, column=3, padx=(25,0), pady=(10,10), sticky=E)




if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
