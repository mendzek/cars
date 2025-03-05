from tkinter import *
from tkinter import ttk
import sqlite3
import LogPassWindow
from SelectedWorkingWindow import *
from NewColumnWindow import *
from NewRowWindow import *
from tkinter import filedialog
from SelectedWorkingWindow import *


class MainWindowOrganisator(Tk):

    sqlPath = ""
    selectedProjects = ""
    selectedProjectsList = list()
    columns = tuple()
    connect = sqlite3.connect
    comboBoxAnswer = ""
    catOrExpert = 0

    def __init__(self):
        super().__init__()

        self.tableValues=list()
        self.headValues=list()
        self.numOfRows=any
        self.selectedProjects = ""

        self.FRTree=ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.FRTree.place(x=0,y=0)
        self.FRLabel = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.FRLabel.place(x=0,y=275)
        self.FRButtons = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.FRButtons.place(x=0,y=340)#532

        self.label=ttk.Label(self.FRLabel,text="-")
        self.label.pack(anchor=N, expand=1)

        self.Tables = ["Кошки", "Клубы", "Эксперты", "Ринги", "Расписание", "Результаты"]
        self.Tables_var = StringVar(value=self.Tables[0])
        self.comboBox = ttk.Combobox(self.FRButtons, textvariable=self.Tables_var, values=self.Tables, state="readonly")
        self.comboBox.grid(row=0, column=0)
        self.comboBox.bind("<<ComboboxSelected>>", self.tableViewInsertEvent)

        self.BTMenuAddCat = ttk.Button(self.FRButtons, text="Добавить кошку", width=20, command=self.menuAddCat)
        self.BTMenuAddCat.grid(row=0, column=1, padx=5, pady=5)
        self.BTMenuAddExpert = ttk.Button(self.FRButtons, text="Добавить эксперта", width=20, command=self.menuAddExpert)
        self.BTMenuAddExpert.grid(row=1, column=1, padx=5, pady=5)
        self.BTDeleteCurrent = ttk.Button(self.FRButtons, text="Удалить строку", width=20, command=self.menuDeleteSelected)
        self.BTDeleteCurrent.grid(row=0, column=2, padx=5, pady=5)
        self.BTClose = ttk.Button(self.FRButtons, text="выход", width=20, command=self.destroy)
        self.BTClose.grid(row=1, column=2, padx=5, pady=5)
        self.BTUpdate = ttk.Button(self.FRButtons, text="Обновить таблицу", width=20, command=self.menuUpdateTable)
        self.BTUpdate.grid(row=2, column=1, columnspan=2, padx=5, pady=5)


        self.title("ProgramPython - Organisator window")
        self.geometry("1150x500")
        self.resizable(False, False)
        sv_ttk.set_theme("dark", self)

        self.sqlPath = "festival.db"
        MainWindowOrganisator.sqlPath = self.sqlPath
        self.connect = sqlite3.connect(self.sqlPath)
        MainWindowOrganisator.connect = self.connect
        self.cursor = self.connect.cursor()
        MainWindowOrganisator.columns = ()
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.comboBox.get()}")
        self.numOfRows = self.cursor.fetchone()[0]
        self.numOfColumns = \
        self.cursor.execute(f"SELECT COUNT(*) FROM pragma_table_info('{self.comboBox.get()}')").fetchone()[0]
        for x in range(self.numOfColumns):
            MainWindowOrganisator.columns += self.cursor.execute(
                f"SELECT name FROM pragma_table_info('{self.comboBox.get()}') Where cid={x}").fetchone()
        self.tree = ttk.Treeview(self.FRTree, columns=MainWindowOrganisator.columns, show="headings")
        self.tree.pack()
        for x in MainWindowOrganisator.columns:
            self.tree.heading(x, text=x)

        self.tree.bind("<<TreeviewSelect>>", self.select)
        self.tree.bind('<Motion>', 'break')


        for x in self.tree.get_children():
            self.tree.delete(x)

        self.headValues.extend(MainWindowOrganisator.columns)
        self.checkTemp = False

        for x in range(self.numOfRows + 1):
            self.cursor.execute(f"SELECT * FROM {self.comboBox.get()} WHERE id={x} ")
            if self.checkTemp == False:
                self.checkTemp = True
            else:
                self.tableValues.append(self.cursor.fetchone())
        for x in self.tableValues:
            try:
                self.tree.insert("", END, values=x)
            except:
                pass
        for x in range(self.numOfColumns+1):
            if self.comboBox.get() == "Кошки":
                self.tree.column("#1", stretch=NO, width=30)
                self.tree.column("#2", stretch=NO, width=80)
                self.tree.column("#3", stretch=NO, width=90)
                self.tree.column("#4", stretch=NO, width=90)
                self.tree.column("#5", stretch=NO, width=70)
                self.tree.column("#6", stretch=NO, width=160)
                self.tree.column("#7", stretch=NO, width=150)
                self.tree.column("#8", stretch=NO, width=150)
                self.tree.column("#9", stretch=NO, width=150)
                self.tree.column("#10", stretch=NO, width=150)
        for x in MainWindowOrganisator.columns:
            self.tree.heading(f"{x}", anchor=W)


    def menuAddCat(self):
        MainWindowOrganisator.catOrExpert = 0
        newRowWindow = NewRowWindow()

    def menuAddExpert(self):
        MainWindowOrganisator.catOrExpert = 1
        newRowWindow = NewRowWindow()

    def menuDeleteSelected(self):
        self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                       isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                       cached_statements=128, uri=False)
        self.cursor = self.connect.cursor()
        if self.comboBox.get == "Кошки" or "Эксперты":
            if(len(self.selectedProjectsList)==0):
                self.label["text"] = "Ничего не выбрано"
            else:
                self.cursor.execute(f"DELETE FROM {self.comboBox.get()} WHERE ID = %(first)s" % {"first": self.selectedProjectsList[0]})
                self.connect.commit()
                self.quickFunc()
        else:
            self.label.config(text="можно удалять только из таблиц кошек и экспертов")

    def menuUpdateTable(self):
        self.selectedProjects = None
        self.quickFunc()

    def tableViewInsertEvent(self, event):
        MainWindowOrganisator.comboBoxAnswer = self.comboBox.get()
        self.quickFunc()

    def select(self,event):
        for selected_item in self.tree.selection():
            MainWindowOrganisator.selectedProjectsList.clear()
            self.selectedProjects = ""
            self.item = self.tree.item(selected_item)
            self.project = self.item["values"]
            MainWindowOrganisator.selectedProjectsList = self.item["values"].copy()
            self.selectedProjects = f"{self.selectedProjects}{self.project}\n"
        self.label["text"] = self.selectedProjects
        print(self.selectedProjects)

    def quickFunc(self):
        self.tableValues.clear()
        self.tree.destroy()
        self.sqlPath = "festival.db"
        MainWindowOrganisator.sqlPath = self.sqlPath
        self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                       isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                       cached_statements=128, uri=False)
        MainWindowOrganisator.connect = self.connect
        self.cursor = self.connect.cursor()
        MainWindowOrganisator.columns = ()
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.comboBox.get()}")
        self.numOfRows = self.cursor.fetchone()[0]
        self.numOfColumns=self.cursor.execute(f"SELECT COUNT(*) FROM pragma_table_info('{self.comboBox.get()}')").fetchone()[0]
        for x in range(self.numOfColumns):
            MainWindowOrganisator.columns += self.cursor.execute(f"SELECT name FROM pragma_table_info('{self.comboBox.get()}') Where cid={x}").fetchone()
        self.tree = ttk.Treeview(self.FRTree, columns=MainWindowOrganisator.columns, show="headings")
        self.tree.pack()
        for x in MainWindowOrganisator.columns:
            self.tree.heading(x,text=x)

        self.tree.bind("<<TreeviewSelect>>", self.select)
        self.tree.bind('<Motion>', 'break')

        for x in self.tree.get_children():
            self.tree.delete(x)

        self.headValues.extend(MainWindowOrganisator.columns)
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

        for x in range(self.numOfColumns+1):
            if self.comboBox.get() == "Кошки":
                self.tree.column("#1", stretch=NO, width=30)
                self.tree.column("#2", stretch=NO, width=80)
                self.tree.column("#3", stretch=NO, width=90)
                self.tree.column("#4", stretch=NO, width=90)
                self.tree.column("#5", stretch=NO, width=70)
                self.tree.column("#6", stretch=NO, width=160)
                self.tree.column("#7", stretch=NO, width=150)
                self.tree.column("#8", stretch=NO, width=150)
                self.tree.column("#9", stretch=NO, width=150)
                self.tree.column("#10", stretch=NO, width=150)
            elif self.comboBox.get() == "Клубы":
                self.tree.column("#1", stretch=NO, width=30)
                self.tree.column("#2", stretch=NO, width=120)
                self.tree.column("#3", stretch=NO, width=120)
                self.tree.column("#4", stretch=NO, width=125)
                self.tree.column("#5", stretch=NO, width=140)
                self.tree.column("#6", stretch=NO, width=130)
                self.tree.column("#7", stretch=NO, width=130)
            elif self.comboBox.get() == "Эксперты":
                self.tree.column("#1", stretch=NO, width=30)
                self.tree.column("#2", stretch=NO, width=80)
                self.tree.column("#3", stretch=NO, width=90)
                self.tree.column("#4", stretch=NO, width=165)
                self.tree.column("#5", stretch=NO, width=120)
                self.tree.column("#6", stretch=NO, width=100)
                self.tree.column("#7", stretch=NO, width=150)
            elif self.comboBox.get() == "Ринги":
                self.tree.column("#1", stretch=NO, width=30)
                self.tree.column("#2", stretch=NO, width=180)
                self.tree.column("#3", stretch=NO, width=180)
            elif self.comboBox.get() == "Расписание":
                self.tree.column("#1", stretch=NO, width=30)
                self.tree.column("#2", stretch=NO, width=80)
                self.tree.column("#3", stretch=NO, width=90)
            elif self.comboBox.get() == "Результаты":
                self.tree.column("#1", stretch=NO, width=30)
                self.tree.column("#2", stretch=NO, width=80)
                self.tree.column("#3", stretch=NO, width=90)
                self.tree.column("#4", stretch=NO, width=90)
        for x in MainWindowOrganisator.columns:
            self.tree.heading(f"{x}", anchor=W)


