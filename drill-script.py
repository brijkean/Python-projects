import os, fnmatch, time
     
def list_txts():
    fName = '*.txt'
    fPath = 'C:\\Users\\Brianna\\Documents\\python_projects\\py-drill-100'
    for file in os.listdir():
        if fnmatch.fnmatch(file, fName):
            absPath = os.path.join(fPath, file)
            secs = os.path.getmtime(absPath)
            timestr = time.ctime(secs)
            print("{}  ||  {}".format(file,timestr))
    

if __name__== "__main__":
    list_txts()

