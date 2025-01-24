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
        self.AddMenu.add_cascade(label="Add column", command=self.menuAddColumn, background="#86b300")

        self.mainMenu.add_cascade(label="Add", menu=self.AddMenu, background="#ace600")

        self.mainMenu.add_cascade(label="Update Table", command=self.menuUpdateTable, background="#ace600")
        self.mainMenu.add_cascade(label="Delete selected row", command=self.menuDeleteSelected, background="#ace600")

        self.label=ttk.Label(self,text="asd", background="#86b300")
        self.label.pack(anchor=N, fill=X,expand=1)

        self.Tables = ["Кошки", "Клубы", "Эксперты", "Ринги", "Расписание", "Результаты"]
        self.Tables_var = StringVar(value=self.Tables[0])
        self.comboBox = ttk.Combobox(textvariable=self.Tables_var, values=self.Tables, state="readonly")
        self.comboBox.pack(anchor=NW, padx=6, pady=6)
        self.comboBox.bind("<<ComboboxSelected>>", self.tableViewInsert(True))

        self.title("ProgramPython - Work window")
        self.geometry("1000x500")
        self.config(menu=self.mainMenu, background="#ccff33")



    def menuEdit(self):
            MainWindow.selectedProjects = self.selectedProjects
            selectedWorkingWindow = SelectedWorkingWindow()

    def menuAddRow(self):
        newRowWindow = NewRowWindow()

    def menuAddColumn(self):
        newColumnWindow = NewColumnWindow()

    def menuDeleteSelected(self):
        self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                       isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                       cached_statements=128, uri=False)
        self.cursor = self.connect.cursor()
        if(len(self.selectedProjectsList)==0):
            self.label["text"] = "Ничего не выбрано"
        else:
            self.cursor.execute("DELETE FROM Projects WHERE ID = %(first)s" % {"first": self.selectedProjectsList[0]})
            self.connect.commit()
            mainWindow=MainWindow()
            mainWindow.tableViewInsert(True)
            self.destroy()

    def menuUpdateTable(self):
        self.selectedProjects = None
        mainWindow=MainWindow()
        mainWindow.tableViewInsert(True)
        self.destroy()

    def tableViewInsert(self,sqlPathExist):

        if(sqlPathExist==False):
            self.sqlPath = filedialog.askopenfilename(initialdir="/Projects")
            MainWindow.sqlPath = self.sqlPath
            self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                           isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                           cached_statements=128, uri=False)
            MainWindow.connect = self.connect
            self.cursor = self.connect.cursor()
            MainWindow.columns = ()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Кошки (id INTEGER NOT NULL UNIQUE, Кличка TEXT, Порода TEXT, Возраст INTEGER, Клуб TEXT, Дата_последней_прививки TEXT, ФИО_хозяина TEXT, Номер_Документа INTEGER, Клички_родителей TEXT, PRIMARY KEY(id AUTOINCREMENT));")
            self.connect.commit()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Клубы (id INTEGER NOT NULL UNIQUE, Название_клуба TEXT, Породы_в_клубе TEXT, Количество_кошек INTEGER, Количество_экспертов INTEGER,  Количество_медалей INTEGER, названия_медалей TEXT, PRIMARY KEY(id AUTOINCREMENT));")
            self.connect.commit()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Эксперты (id INTEGER NOT NULL UNIQUE, Фамилия TEXT, Имя TEXT, Специализация_по_породе TEXT, Номер_ринга INTEGER, Клуб TEXT, PRIMARY KEY(id AUTOINCREMENT));")
            self.connect.commit()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Ринги (id INTEGER NOT NULL UNIQUE, Специализация_по_породе TEXT, id_обслуживающих_экспертов TEXT, PRIMARY KEY(id AUTOINCREMENT));")
            self.connect.commit()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Расписание (id INTEGER NOT NULL UNIQUE, id_ринга TEXT, Время TEXT, PRIMARY KEY(id AUTOINCREMENT));")
            self.connect.commit()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Результаты (id INTEGER NOT NULL UNIQUE, id_кошки TEXT, Очки INTEGER, Место INTEGER, PRIMARY KEY(id AUTOINCREMENT));")
            self.connect.commit()
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
        else:
            self.connect = sqlite3.connect("festival.db")
            self.cursor = self.connect.cursor()
            MainWindow.columns = ()
            self.cursor.execute(f"SELECT COUNT(*) FROM {self.comboBox.get()}")
            self.numOfRows = self.cursor.fetchone()[0]
            self.numOfColumns = self.cursor.execute(f"SELECT COUNT(*) FROM pragma_table_info('{self.comboBox.get()}')").fetchone()[0]
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




