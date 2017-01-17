# -*- coding: utf-8 -*-

from PIL import Image, ImageTk
from tkinter import Tk, Frame, Menu
from tkinter import PanedWindow, BOTH, VERTICAL
from tkinter import Listbox, EXTENDED, SINGLE, END
from tkinter import Button, LEFT, TOP, X, FLAT, RAISED
from tkinter import Text, WORD, Label

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
        #AddButton.pack(side=LEFT, padx=2, pady=2)
        AddButton.grid(sticky="E")
        #toolbar.pack(side=TOP, fill=X)
        toolbar.grid(row=0, rowspan=1)
        self.parent.config(menu=menubar)
        #self.pack()
        #self.grid()

        m1 = PanedWindow()
        m1["bg"] = "blue"
        #m1.pack(fill=BOTH, expand=1)
        m2 = PanedWindow(m1, orient=VERTICAL)
        m2["bg"] = "black"
        m1.add(m2)
        #m2.grid(row=2, columnspan=3)

        listbox1=Listbox(m1,height=5,width=50,selectmode=SINGLE)
        conn = sqlite3.connect('data.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Films order by Name asc')
        row = cur.fetchone()
        while row is not None:
            listbox1.insert(END,row[0])
            row = cur.fetchone()
        cur.close()
        conn.close()
        m1.add(listbox1)
        m1.grid(row=2, columnspan=1, rowspan=5)

        frame1 = Frame(m2, width=250, heigh=100, bg='red', bd=1)
        frame2 = Frame(m2, bg = 'green', bd=5)
        label_year = Label(frame2, font = 'Arial 12', text = 'Год:')
        label_genre = Label(frame2, font = 'Arial 12', text = 'Жанр:')
        #frame1.pack(side='left')
        frame1.grid(column=1, row=1, rowspan=3, sticky = "W"+"E"+"N"+"S")
        #frame2.pack()
        frame2.grid(column=2, row=1, columnspan=2, sticky = "W"+"E"+"N"+"S")
        #label_year.pack(side='left')
        label_year.grid()
        #label_genre.pack(side='top')
        label_genre.grid()
        text1 = Text(frame2, font = 'Arial 14', wrap = WORD)
        #text1.pack()
        text1.grid()
        
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
