from tkinter import *
from tkinter import ttk
import sqlite3
import LogPassWindow
from MainWindowOrganisator import *


class NewColumnWindow(Tk):

    def __init__(self):
        super().__init__()

        self.list = ["Integer","Text"]

        self.title("ProgramPython - New column")
        self.geometry("350x300")

        self.entry = ttk.Entry(self, background="#ccff33")
        self.entry.pack(expand=1, side=LEFT)

        self.BT_OK = ttk.Button(self, text="Сохранить", command=self.BT_OK)
        self.BT_OK.pack(expand=1, side=BOTTOM)

        self.config(background="#ccff33")

    def BT_OK(self):
        self.connect = LogPassWindow.MainWindowOrganisator.connect
        self.cursor = self.connect.cursor()
        self.cursor.execute("ALTER TABLE Projects ADD %(first)s %(second)s" % {"first":self.entry.get(), "second":"TEXT"})
        self.connect.commit()
        self.destroy()



