from tkinter import *
from tkinter import ttk
import sqlite3

import LogPassWindow
from SelectedWorkingWindow import *
from NewColumnWindow import *
from NewRowWindow import *
from tkinter import filedialog

class MainWindow(Tk):

    sqlPath = ""
    selectedProjects = ""
    selectedProjectsList = list()
    columns = tuple()
    connect = sqlite3.connect
    comboBoxAnswer = ""

    def __init__(self):
        super().__init__()

        self.tableValues=list()
        self.headValues=list()
        self.numOfRows=any
        self.selectedProjects = ""

        self.mainMenu = Menu(self, background="#ace600")
        self.editMenu = Menu(self,tearoff=0)
        self.editMenu.add_cascade(label="Edit table",command=self.menuEdit, background="#86b300")
        self.mainMenu.add_cascade(label="Edit",menu=self.editMenu, background="#86b300")

        self.AddMenu = Menu(self, tearoff=0, background="#ace600")
        self.AddMenu.add_cascade(label="Add row", command=self.menuAddRow, background="#86b300")

        self.mainMenu.add_cascade(label="Add", menu=self.AddMenu, background="#ace600")

        self.mainMenu.add_cascade(label="Update Table", command=self.menuUpdateTable, background="#ace600")
        self.mainMenu.add_cascade(label="Delete selected row", command=self.menuDeleteSelected, background="#ace600")

        self.label=ttk.Label(self,text="asd", background="#86b300")
        self.label.pack(anchor=N, fill=X,expand=1)

        self.Tables = ["Кошки", "Клубы", "Эксперты", "Ринги", "Расписание", "Результаты"]
        self.Tables_var = StringVar(value=self.Tables[0])
        self.comboBox = ttk.Combobox(textvariable=self.Tables_var, values=self.Tables, state="readonly")
        self.comboBox.pack(anchor=NW, padx=6, pady=6)
        self.comboBox.bind("<<ComboboxSelected>>", self.tableViewInsertEvent)

        self.title("ProgramPython - Work window")
        self.geometry("1000x500")
        self.config(menu=self.mainMenu, background="#ccff33")

        self.sqlPath = "festival.db"
        MainWindow.sqlPath = self.sqlPath
        self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                       isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                       cached_statements=128, uri=False)
        MainWindow.connect = self.connect
        self.cursor = self.connect.cursor()
        MainWindow.columns = ()
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.comboBox.get()}")
        self.numOfRows = self.cursor.fetchone()[0]
        self.numOfColumns = \
        self.cursor.execute(f"SELECT COUNT(*) FROM pragma_table_info('{self.comboBox.get()}')").fetchone()[0]
        for x in range(self.numOfColumns):
            MainWindow.columns += self.cursor.execute(
                f"SELECT name FROM pragma_table_info('{self.comboBox.get()}') Where cid={x}").fetchone()
        self.tree = ttk.Treeview(self, columns=MainWindow.columns, show="headings")
        self.tree.pack(anchor=S, fill=BOTH, expand=1)
        for x in MainWindow.columns:
            self.tree.heading(x, text=x)

        self.tree.bind("<<TreeviewSelect>>", self.select)

        for x in self.tree.get_children():
            self.tree.delete(x)

        self.headValues.extend(MainWindow.columns)
        self.checkTemp = False

        for x in range(self.numOfRows + 1):
            self.cursor.execute(f"SELECT * FROM {self.comboBox.get()} WHERE id={x}")
            if self.checkTemp == False:
                self.checkTemp = True
            else:
                self.tableValues.append(self.cursor.fetchone())
        for x in self.tableValues:
            try:
                self.tree.insert("", END, values=x)
            except:
                pass


        self.scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.tree.yview)
        self.scrollbar.pack(side=BOTTOM, fill=X)

    def menuEdit(self):
            MainWindow.selectedProjects = self.selectedProjects
            selectedWorkingWindow = SelectedWorkingWindow()

    def menuAddRow(self):
        newRowWindow = NewRowWindow()

    def menuDeleteSelected(self):
        self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                       isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                       cached_statements=128, uri=False)
        self.cursor = self.connect.cursor()
        if(len(self.selectedProjectsList)==0):
            self.label["text"] = "Ничего не выбрано"
        else:
            self.cursor.execute(f"DELETE FROM {self.comboBox.get()} WHERE ID = %(first)s" % {"first": self.selectedProjectsList[0]})
            self.connect.commit()
            self.quickFunc()

    def menuUpdateTable(self):
        self.selectedProjects = None
        self.quickFunc()

    def tableViewInsertEvent(self, event):
        MainWindow.comboBoxAnswer = self.comboBox.get()
        self.quickFunc()

    def select(self,event):
        for selected_item in self.tree.selection():
            MainWindow.selectedProjectsList.clear()
            self.selectedProjects = ""
            self.item = self.tree.item(selected_item)
            self.project = self.item["values"]
            MainWindow.selectedProjectsList = self.item["values"].copy()
            self.selectedProjects = f"{self.selectedProjects}{self.project}\n"
        self.label["text"] = self.selectedProjects
        print(self.selectedProjects)

    def quickFunc(self):
        self.tableValues.clear()
        self.tree.destroy()
        self.sqlPath = "festival.db"
        MainWindow.sqlPath = self.sqlPath
        self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                       isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                       cached_statements=128, uri=False)
        MainWindow.connect = self.connect
        self.cursor = self.connect.cursor()
        MainWindow.columns = ()
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.comboBox.get()}")
        self.numOfRows = self.cursor.fetchone()[0]
        self.numOfColumns=self.cursor.execute(f"SELECT COUNT(*) FROM pragma_table_info('{self.comboBox.get()}')").fetchone()[0]
        for x in range(self.numOfColumns):
            MainWindow.columns += self.cursor.execute(f"SELECT name FROM pragma_table_info('{self.comboBox.get()}') Where cid={x}").fetchone()
        self.tree = ttk.Treeview(self, columns=MainWindow.columns, show="headings")
        self.tree.pack(anchor=S,fill=BOTH, expand=1)
        for x in MainWindow.columns:
            self.tree.heading(x,text=x)

        self.tree.bind("<<TreeviewSelect>>", self.select)

        for x in self.tree.get_children():
            self.tree.delete(x)

        self.headValues.extend(MainWindow.columns)
        self.checkTemp=False

        for x in range(self.numOfRows+1):
            self.cursor.execute(f"SELECT * FROM {self.comboBox.get()} WHERE id={x}")
            if self.checkTemp==False:
                self.checkTemp=True
            else:
                self.tableValues.append(self.cursor.fetchone())
        for x in self.tableValues:
            try:
                self.tree.insert("", END, values=x)
            except:
                pass


