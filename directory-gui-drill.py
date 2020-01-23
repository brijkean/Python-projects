import os, fnmatch, time, shutil, sqlite3

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

        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        gui(self)



def gui(self):
    self.txt1 = tk.Entry(self.master, width=50, text = '')
    self.txt1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(30,0),pady=(43,0),sticky=N+E+W)
    self.txt2 = tk.Entry(self.master, width=50, text = '')
    self.txt2.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(30,0),pady=(13,0),sticky=N+E+W)
    
    self.btn_browse1 = tk.Button(self.master, width=10, height=1, text='Browse...', command= lambda: selectDir(self))
    self.btn_browse1.grid(row=0, column=0, padx=(25,0), pady=(40,0), sticky=W)
    self.btn_browse2 = tk.Button(self.master, width=10, height=1, text='Browse...', command= lambda: selectDst(self))
    self.btn_browse2.grid(row=1, column=0, padx=(25,0), pady=(10,0), sticky=W)

    self.btn_close = tk.Button(self.master, width=12, height=2, text='Check for files...', command= lambda: move_txts(self))
    self.btn_close.grid(row=3, column=3, padx=(25,0), pady=(10,10), sticky=E)


def selectDir(self):
    dirname = tk.filedialog.askdirectory()
    self.txt1.delete(0,END)
    self.txt1.insert(0,"{}".format(dirname))

def selectDst(self):
    dirname = tk.filedialog.askdirectory()
    self.txt2.delete(0,END)
    self.txt2.insert(0,"{}".format(dirname))

        
def move_txts(self):
    fName = '*.txt'
    fPath = self.txt1.get()
    for file in os.listdir(fPath):
        if fnmatch.fnmatch(file, fName):
            absPath = os.path.join(fPath, file).replace("\\","/")
            secs = os.path.getmtime(absPath)
            timestr = time.ctime(secs)
            
            dst = self.txt2.get()
            shutil.move(absPath,dst)
    createDB(self)
    


#----DB creation and query----#

def createDB(self):
    conn = sqlite3.connect('newdir_txts.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_filename TEXT, \
                col_mtime TEXT, \
                UNIQUE(col_filename,col_mtime) \
                )")
        conn.commit()
    conn.close()
    insertData(self)
    

def insertData(self):
    fName = '*.txt'
    dst = self.txt2.get()
    conn = sqlite3.connect('newdir_txts.db')
    with conn:
            cur = conn.cursor()
            for file in os.listdir(dst):
                if fnmatch.fnmatch(file, fName):
                    #check if file is already in db
                    cur.execute("""SELECT COUNT(col_filename) FROM tbl_files WHERE col_filename = '{}'""".format(file))
                    count = cur.fetchone()[0]
                    
                    absPath = os.path.join(dst, file).replace("\\","/")
                    secs = os.path.getmtime(absPath)
                    timestr = time.ctime(secs)
                    if count == 0:
                        cur.execute("INSERT INTO tbl_files(col_filename,col_mtime) VALUES (?,?)",(file,timestr,))
                        conn.commit()
            if count == 0:
                print("\nAdding new files...")
    conn.close()
    queryDB(self)


def queryDB(self):
    conn = sqlite3.connect('newdir_txts.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_filename, col_mtime FROM tbl_files")
        varFiles = cur.fetchall()
        i = 0
        print("\n.txt files in the database:   ||   Time last modified:")
        for item in varFiles:
            dsp = "{}        {}".format(item[0],item[1])
            print(dsp)
    


if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
