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
            self.label1 = ttk.Label(self, text="id", background="#ccff33")
            self.label1.grid(row=0, column=0, pady=10, padx=10)
            self.LabelList.append(self.label1)
            self.entry1 = ttk.Entry(self, name="entry_" + str(0), state=NORMAL, background="#ccff33")
            self.entry1.grid(row=1, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry1)
            self.label2 = ttk.Label(self, text="Кличка", background="#ccff33")
            self.label2.grid(row=2, column=0, pady=10, padx=10)
            self.LabelList.append(self.label2)
            self.entry2 = ttk.Entry(self, name="entry_" + str(1), state=NORMAL, background="#ccff33")
            self.entry2.grid(row=3, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry2)
            self.label3 = ttk.Label(self, text="Порода", background="#ccff33")
            self.label3.grid(row=4, column=0, pady=10, padx=10)
            self.LabelList.append(self.label3)
            self.entry3 = ttk.Entry(self, name="entry_" + str(2), state=NORMAL, background="#ccff33")
            self.entry3.grid(row=5, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry3)
            self.label4 = ttk.Label(self, text="Возраст", background="#ccff33")
            self.label4.grid(row=6, column=0, pady=10, padx=10)
            self.LabelList.append(self.label4)
            self.entry4 = ttk.Entry(self, name="entry_" + str(3), state=NORMAL, background="#ccff33")
            self.entry4.grid(row=7, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry4)
            self.label5 = ttk.Label(self, text="Клуб", background="#ccff33")
            self.label5.grid(row=8, column=0, pady=10, padx=10)
            self.LabelList.append(self.label5)
            self.entry5 = ttk.Entry(self, name="entry_" + str(4), state=NORMAL, background="#ccff33")
            self.entry5.grid(row=9, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry5)
            self.label6 = ttk.Label(self, text="Дата последней прививки", background="#ccff33")
            self.label6.grid(row=0, column=1, pady=10, padx=10)
            self.LabelList.append(self.label6)
            self.entry6 = ttk.Entry(self, name="entry_" + str(5), state=NORMAL, background="#ccff33")
            self.entry6.grid(row=1, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry6)
            self.label7 = ttk.Label(self, text="ФИО хозяйна", background="#ccff33")
            self.label7.grid(row=2, column=1, pady=10, padx=10)
            self.LabelList.append(self.label7)
            self.entry7 = ttk.Entry(self, name="entry_" + str(6), state=NORMAL, background="#ccff33")
            self.entry7.grid(row=3, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry7)
            self.label8 = ttk.Label(self, text="Номер документа", background="#ccff33")
            self.label8.grid(row=4, column=1, pady=10, padx=10)
            self.LabelList.append(self.label8)
            self.entry8 = ttk.Entry(self, name="entry_" + str(7), state=NORMAL, background="#ccff33")
            self.entry8.grid(row=5, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry8)
            self.label9 = ttk.Label(self, text="Клички родителей", background="#ccff33")
            self.label9.grid(row=6, column=1, pady=10, padx=10)
            self.LabelList.append(self.label9)
            self.entry9 = ttk.Entry(self, name="entry_" + str(8), state=NORMAL, background="#ccff33")
            self.entry9.grid(row=7, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry9)
            self.label10 = ttk.Label(self, text="В соревновании", background="#ccff33")
            self.label10.grid(row=8, column=1, pady=10, padx=10)
            self.LabelList.append(self.label10)
            self.entry10 = ttk.Entry(self, name="entry_" + str(9), state=NORMAL, background="#ccff33")
            self.entry10.grid(row=9, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry10)
        if LogPassWindow.MainWindowOrganisator.catOrExpert == 1:                    # СДЕЛАТЬ ЭКСПЕРТОВ
            self.nameOfTable = "Эксперты"
            self.label1 = ttk.Label(self, text="id", background="#ccff33")
            self.label1.grid(row=0, column=0, pady=10, padx=10)
            self.LabelList.append(self.label1)
            self.entry1 = ttk.Entry(self, name="entry_" + str(0), state=NORMAL, background="#ccff33")
            self.entry1.grid(row=1, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry1)
            self.label2 = ttk.Label(self, text="Фамилия", background="#ccff33")
            self.label2.grid(row=2, column=0, pady=10, padx=10)
            self.LabelList.append(self.label2)
            self.entry2 = ttk.Entry(self, name="entry_" + str(1), state=NORMAL, background="#ccff33")
            self.entry2.grid(row=3, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry2)
            self.label3 = ttk.Label(self, text="Имя", background="#ccff33")
            self.label3.grid(row=4, column=0, pady=10, padx=10)
            self.LabelList.append(self.label3)
            self.entry3 = ttk.Entry(self, name="entry_" + str(2), state=NORMAL, background="#ccff33")
            self.entry3.grid(row=5, column=0, pady=10, padx=10)
            self.entrysList.append(self.entry3)
            self.label4 = ttk.Label(self, text="Специализация по породе", background="#ccff33")
            self.label4.grid(row=0, column=1, pady=10, padx=10)
            self.LabelList.append(self.label4)
            self.entry4 = ttk.Entry(self, name="entry_" + str(3), state=NORMAL, background="#ccff33")
            self.entry4.grid(row=1, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry4)
            self.label5 = ttk.Label(self, text="Номер ринга", background="#ccff33")
            self.label5.grid(row=2, column=1, pady=10, padx=10)
            self.LabelList.append(self.label5)
            self.entry5 = ttk.Entry(self, name="entry_" + str(4), state=NORMAL, background="#ccff33")
            self.entry5.grid(row=3, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry5)
            self.label6 = ttk.Label(self, text="Клуб", background="#ccff33")
            self.label6.grid(row=4, column=1, pady=10, padx=10)
            self.LabelList.append(self.label6)
            self.entry6 = ttk.Entry(self, name="entry_" + str(5), state=NORMAL, background="#ccff33")
            self.entry6.grid(row=5, column=1, pady=10, padx=10)
            self.entrysList.append(self.entry6)
            self.label7 = ttk.Label(self, text="В саревновании", background="#ccff33")
            self.label7.grid(row=6, column=0, pady=10, padx=10, columnspan=2)
            self.LabelList.append(self.label7)
            self.entry7 = ttk.Entry(self, name="entry_" + str(6), state=NORMAL, background="#ccff33")
            self.entry7.grid(row=7, column=0, pady=10, padx=10, columnspan=2)
            self.entrysList.append(self.entry7)

        self.title("ProgramPython - New row")
        self.geometry("350x450")
        self.resizable(False, False)



        self.BT_OK = ttk.Button(self, text="Сохранить", command=self.BT_OK)
        self.BT_OK.grid(row=10, column=0, pady=10, padx=10, columnspan=2)

        self.config(background="#ccff33")

    def BT_OK(self):
        self.sqlPath = "festival.db"
        self.connect = sqlite3.connect(self.sqlPath)
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