import sqlite3
from tkinter import *
from tkinter import ttk
import LogPassWindow


class NewRowWindow(Tk):

    def __init__(self):
        super().__init__()

        self.list = ["Integer", "Text"]
        self.LabelList = list()
        self.entrysList = list()
        if LogPassWindow.MainWindowOrganisator.catOrExpert == 0:
            self.nameOfTable = "Кошки"
        if LogPassWindow.MainWindowOrganisator.catOrExpert == 1:
            self.nameOfTable = "Эксперты"
        self.title("ProgramPython - New row")
        self.geometry("800x300")

        for x in range(len(LogPassWindow.MainWindowOrganisator.columns)):
            self.label = ttk.Label(self, text=f"{LogPassWindow.MainWindowOrganisator.columns[x]}", background="#ccff33")
            self.label.pack(expand=1)
            self.LabelList.append(self.label)
            self.entry = ttk.Entry(self,name="entry_"+str(x), state=NORMAL, background="#ccff33")
            self.entry.pack(expand=1)
            self.entrysList.append(self.entry)

        self.BT_OK = ttk.Button(self, text="Сохранить", command=self.BT_OK)
        self.BT_OK.pack(expand=1, side=BOTTOM)

        self.config(background="#ccff33")

    def BT_OK(self):
        self.sqlPath = "festival.db"
        self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                       isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                       cached_statements=128, uri=False)
        self.cursor = self.connect.cursor()
        self.strTemp = "("
        self.check=True
        for x in range(len(LogPassWindow.MainWindowOrganisator.columns)):
            if self.check==True:
                self.strTemp += f"'{LogPassWindow.MainWindowOrganisator.columns[x]}'"
                self.check=False
            else:
                self.strTemp += ", "
                self.strTemp += f"'{LogPassWindow.MainWindowOrganisator.columns[x]}'"
        self.strTemp += ")"

        self.strTemp2 = "("
        self.check=True
        for x in range(len(self.entrysList)):
            if self.check==True:
                self.strTemp2 += f"'{self.entrysList[x].get()}'"
                self.check=False
            else:
                self.strTemp2 += ", "
                self.strTemp2 += f"'{self.entrysList[x].get()}'"
        self.strTemp2 += ")"

        self.cursor.execute("INSERT INTO %(third)s%(first)s VALUES %(second)s" % {"first": self.strTemp, "second": self.strTemp2, "third": self.nameOfTable})
        self.connect.commit()
        self.destroy()