from tkinter import *
from tkinter import ttk
import LogPassWindow


class NewRowWindow(Tk):

    def __init__(self):
        super().__init__()

        self.list = ["Integer", "Text"]
        self.LabelList = list()
        self.entrysList = list()
        self.title("ProgramPython - New row")
        self.geometry("800x300")

        for x in range(len(LogPassWindow.MainWindow.columns)):
            self.label = ttk.Label(self,text=f"{LogPassWindow.MainWindow.columns[x]}", background="#ccff33")
            self.label.pack(expand=1)
            self.LabelList.append(self.label)
            self.entry = ttk.Entry(self,name="entry_"+str(x), state=NORMAL, background="#ccff33")
            self.entry.pack(expand=1)
            self.entrysList.append(self.entry)

        self.BT_OK = ttk.Button(self, text="Сохранить", command=self.BT_OK)
        self.BT_OK.pack(expand=1, side=BOTTOM)

        self.config(background="#ccff33")

    def BT_OK(self):
        self.connect = LogPassWindow.mainWindow.connect
        self.cursor = self.connect.cursor()
        self.strTemp = "("
        self.check=True
        for x in range(len(LogPassWindow.MainWindow.columns)):
            if self.check==True:
                self.strTemp += f"'{LogPassWindow.MainWindow.columns[x]}'"
                self.check=False
            else:
                self.strTemp += ", "
                self.strTemp += f"'{LogPassWindow.MainWindow.columns[x]}'"
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

        self.cursor.execute("INSERT INTO Projects%(first)s VALUES %(second)s" % {"first": self.strTemp, "second": self.strTemp2})
        self.connect.commit()
        self.destroy()