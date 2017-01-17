# -*- coding: utf-8 -*-

from PIL import Image, ImageTk
from tkinter import Tk, Frame, Menu
from tkinter import PanedWindow, BOTH, VERTICAL
from tkinter import Listbox, EXTENDED, SINGLE, END
from tkinter import Button, LEFT, TOP, X, FLAT, RAISED

import sys
import sqlite3

class MainMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Filmoteka")
        
        menubar = Menu(self.parent)
        fileMenu = Menu(menubar, tearoff = 0)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        self.parent.config(menu=menubar)

        toolbar = Frame(self.parent, bd=1, relief=RAISED)
        self.img = Image.open("add.png")
        eimg = ImageTk.PhotoImage(self.img)  
        AddButton = Button(toolbar, image=eimg, relief=FLAT, command=self.Add) #
        AddButton.image = eimg
        AddButton.pack(side=LEFT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)
        self.parent.config(menu=menubar)
        self.pack()

        m1 = PanedWindow()
        m1["bg"] = "blue"
        m1.pack(fill=BOTH, expand=1)

        listbox1=Listbox(m1,height=5,width=50,selectmode=SINGLE)
        conn = sqlite3.connect('data.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Films order by Name asc')
        row = cur.fetchone()
        while row is not None:
            listbox1.insert(END,row[0])
            row = cur.fetchone()

        #list1=["11111","22222","33333","44444"]
        cur.close()
        conn.close()

        #for i in list1:
            #listbox1.insert(END,i)
        m1.add(listbox1)
        m2 = PanedWindow(m1, orient=VERTICAL)
        m2["bg"] = "black"
        m1.add(m2)

    def Add():
        pass

    def onExit(self):
        self.quit()

def main():
    root = Tk()
    app = MainMenu(root)
    if sys.platform != 'linux2':
        root.wm_state('zoomed')
    else:
        root.wm_attributes('-zoomed', True)

    root.mainloop()

if __name__ == '__main__':
    main()
