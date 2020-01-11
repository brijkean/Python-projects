import sqlite3

def createDB():
    conn = sqlite3.connect('drill.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_filename TEXT)")
        conn.commit()
    conn.close()
    insertData()

def insertData():
    conn = sqlite3.connect('drill.db')
    with conn:
        cur = conn.cursor()
        fileList = ('information.docx','Hello.txt','myImage.png', \
                    'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
        for item in fileList:
            if '.txt' in item:
                cur.execute("INSERT INTO tbl_files(col_filename) VALUES (?)", \
                        (item,))
                conn.commit()
    conn.close()


def queryDB():
    conn = sqlite3.connect('drill.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_filename FROM tbl_files")
        varFiles = cur.fetchall()
        i = 0
        print("List of .txt files in the database:")
        for item in varFiles:
            dsp = "{}".format(item[i])
            print(dsp)


if __name__ == "__main__":
    createDB()
    queryDB()
