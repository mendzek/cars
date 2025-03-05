import sqlite3
from tkinter import *
from tkinter import ttk
import LogPassWindow
import sv_ttk


class NewRowWindow(Tk):

    def __init__(self):
        super().__init__()

        self.sqlPath = "festival.db"
        self.connect = sqlite3.connect(self.sqlPath)
        self.cursor = self.connect.cursor()
        self.columns = ()
        self.list = ["Integer", "Text"]
        self.LabelList = list()
        self.entrysList = list()
        if LogPassWindow.MainWindowOrganisator.catOrExpert == 0:
            self.nameOfTable = "Кошки"
            for x in range(self.cursor.execute(f"SELECT COUNT(*) FROM pragma_table_info('Кошки')").fetchone()[0]):
                self.columns += self.cursor.execute(f"SELECT name FROM pragma_table_info('Кошки') Where cid={x}").fetchone()
            self.label2 = ttk.Label(self, text="Кличка")
            self.label2.grid(row=0, column=0, pady=10, padx=10)
            self.LabelList.append(self.label2)
            self.entry2 = ttk.Entry(self, name="entry_" + str(1), state=NORMAL)
            self.entry2.grid(row=1, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry2)
            self.label3 = ttk.Label(self, text="Порода")
            self.label3.grid(row=0, column=1, pady=10, padx=10)
            self.LabelList.append(self.label3)
            self.entry3 = ttk.Entry(self, name="entry_" + str(2), state=NORMAL)
            self.entry3.grid(row=1, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry3)
            self.label4 = ttk.Label(self, text="Возраст")
            self.label4.grid(row=2, column=0, pady=10, padx=10)
            self.LabelList.append(self.label4)
            self.entry4 = ttk.Entry(self, name="entry_" + str(3), state=NORMAL)
            self.entry4.grid(row=3, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry4)
            self.label5 = ttk.Label(self, text="Клуб")
            self.label5.grid(row=2, column=1, pady=10, padx=10)
            self.LabelList.append(self.label5)
            self.entry5 = ttk.Entry(self, name="entry_" + str(4), state=NORMAL)
            self.entry5.grid(row=3, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry5)
            self.label6 = ttk.Label(self, text="Дата последней прививки")
            self.label6.grid(row=4, column=0, pady=10, padx=10)
            self.LabelList.append(self.label6)
            self.entry6 = ttk.Entry(self, name="entry_" + str(5), state=NORMAL)
            self.entry6.grid(row=5, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry6)
            self.label7 = ttk.Label(self, text="ФИО хозяйна")
            self.label7.grid(row=4, column=1, pady=10, padx=10)
            self.LabelList.append(self.label7)
            self.entry7 = ttk.Entry(self, name="entry_" + str(6), state=NORMAL)
            self.entry7.grid(row=5, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry7)
            self.label8 = ttk.Label(self, text="Номер документа")
            self.label8.grid(row=6, column=0, pady=10, padx=10)
            self.LabelList.append(self.label8)
            self.entry8 = ttk.Entry(self, name="entry_" + str(7), state=NORMAL)
            self.entry8.grid(row=7, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry8)
            self.label9 = ttk.Label(self, text="Клички родителей")
            self.label9.grid(row=6, column=1, pady=10, padx=10)
            self.LabelList.append(self.label9)
            self.entry9 = ttk.Entry(self, name="entry_" + str(8), state=NORMAL)
            self.entry9.grid(row=7, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry9)
            self.label10 = ttk.Label(self, text="В соревновании")
            self.label10.grid(row=8, column=0, pady=10, padx=10, columnspan=2)
            self.LabelList.append(self.label10)
            self.entry10 = ttk.Entry(self, name="entry_" + str(9), state=NORMAL)
            self.entry10.grid(row=9, column=0, pady=10, padx=10, columnspan=2)
            self.entrysList.append(self.entry10)
        if LogPassWindow.MainWindowOrganisator.catOrExpert == 1:
            self.nameOfTable = "Эксперты"
            for x in range(self.cursor.execute(f"SELECT COUNT(*) FROM pragma_table_info('Эксперты')").fetchone()[0]):
                self.columns += self.cursor.execute(f"SELECT name FROM pragma_table_info('Эксперты') Where cid={x}").fetchone()
            self.label2 = ttk.Label(self, text="Фамилия")
            self.label2.grid(row=0, column=0, pady=10, padx=10)
            self.LabelList.append(self.label2)
            self.entry2 = ttk.Entry(self, name="entry_" + str(1), state=NORMAL)
            self.entry2.grid(row=1, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry2)
            self.label3 = ttk.Label(self, text="Имя")
            self.label3.grid(row=0, column=1, pady=10, padx=10)
            self.LabelList.append(self.label3)
            self.entry3 = ttk.Entry(self, name="entry_" + str(2), state=NORMAL)
            self.entry3.grid(row=1, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry3)
            self.label4 = ttk.Label(self, text="Специализация по породе")
            self.label4.grid(row=3, column=0, pady=10, padx=10)
            self.LabelList.append(self.label4)
            self.entry4 = ttk.Entry(self, name="entry_" + str(3), state=NORMAL)
            self.entry4.grid(row=4, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry4)
            self.label5 = ttk.Label(self, text="Номер ринга")
            self.label5.grid(row=3, column=1, pady=10, padx=10)
            self.LabelList.append(self.label5)
            self.entry5 = ttk.Entry(self, name="entry_" + str(4), state=NORMAL)
            self.entry5.grid(row=4, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry5)
            self.label6 = ttk.Label(self, text="Клуб")
            self.label6.grid(row=5, column=0, pady=10, padx=10)
            self.LabelList.append(self.label6)
            self.entry6 = ttk.Entry(self, name="entry_" + str(5), state=NORMAL)
            self.entry6.grid(row=6, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry6)
            self.label7 = ttk.Label(self, text="В саревновании")
            self.label7.grid(row=5, column=1, pady=10, padx=10)
            self.LabelList.append(self.label7)
            self.entry7 = ttk.Entry(self, name="entry_" + str(6), state=NORMAL)
            self.entry7.grid(row=6, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry7)

        self.title("ProgramPython - New row")
        self.geometry("400x500")
        self.resizable(False, False)
        sv_ttk.set_theme("dark", self)


        self.BT_OK = ttk.Button(self, text="Сохранить", command=self.BT_OK)
        self.BT_OK.grid(row=10, column=0, pady=10, padx=10, columnspan=2)

    def BT_OK(self):
        self.strTemp = "("
        self.check=True
        for x in range(len(self.columns)):

            if self.check==True:
                self.strTemp += f"'id'"
                self.check=False
            else:
                self.strTemp += ", "
                self.strTemp += f"'{self.columns[x]}'"
        self.strTemp += ")"

        self.strTemp2 = "("
        self.check=True
        for x in range(len(self.entrysList)):
            if self.check==True:
                self.strTemp2 += f"'{self.cursor.execute(f"SELECT id FROM {self.nameOfTable} ORDER BY id desc").fetchone()[0]+1}'"
                self.strTemp2 += ", "
                self.strTemp2 += f"'{self.entrysList[x].get()}'"
                self.check=False
            else:
                self.strTemp2 += ", "
                self.strTemp2 += f"'{self.entrysList[x].get()}'"
        self.strTemp2 += ")"

        self.cursor.execute("INSERT INTO %(third)s%(first)s VALUES %(second)s" % {"first": self.strTemp, "second": self.strTemp2, "third": self.nameOfTable})
        self.connect.commit()
        self.destroy()