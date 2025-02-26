from tkinter import *
from tkinter import ttk
import sqlite3
import MainWindowOrganisator
from tkinter.messagebox import showwarning
from MainWindowOrganisator import *
from LogPassWindow import *
import LogPassWindow

class SelectedWorkingWindow(Tk):

    textFromTextBox=""
    LogPassWindow=LogPassWindow
    checkIfDestroed = False

    def __init__(self):
        super().__init__()

        self.connect = LogPassWindow.MainWindowOrganisator.connect

        self.entrysList = list()
        self.LabelList = list()
        self.selectedProjectsList = LogPassWindow.MainWindowOrganisator.selectedProjectsList.copy()
        self.columns = LogPassWindow.MainWindowOrganisator.columns

        self.title("ProgramPython - Selected work window")
        self.geometry("800x300")

        self.label = ttk.Label(self, text="Измените строку в окне ниже. Нажмите \"Сохранить\" когда закончите", background="#ccff33")
        self.label.pack(expand=1,side=TOP)

        self.config(background="#ccff33")

        for x in range(len(self.selectedProjectsList)):
            self.label = ttk.Label(self, text=f"{LogPassWindow.MainWindowOrganisator.columns[x]}", background="#ccff33")
            self.label.pack(expand=1)
            self.LabelList.append(self.label)
            self.entry = ttk.Entry(self,name="entry_"+str(x), state=NORMAL, background="#ccff33")
            self.entry.insert(0,f"{self.selectedProjectsList[x]}")
            self.entry.pack(expand=1)
            self.entrysList.append(self.entry)

        self.BT_save = ttk.Button(self, text="Сохранить", command=self.BT_save)
        self.BT_save.pack(expand=1,side=BOTTOM)

    def BT_save(self):
        self.cursor = self.connect.cursor()
        for x in range(len(self.columns)):
            self.cursor.execute("UPDATE Projects SET %(first)s = '%(second)s' WHERE ID = '%(third)s'" % {"first": self.columns[x], "second": self.entrysList[x].get(), "third": self.selectedProjectsList[0]})
            self.connect.commit()
        SelectedWorkingWindow.checkIfDestroed=True
        self.destroy()