import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo, askyesno
from MainWindow import *
import sqlite3
import random
import sys


connectLogPass = sqlite3.connect("LogPass.db")
cursorLogPass = connectLogPass.cursor()
cursorLogPass.execute("CREATE TABLE IF NOT EXISTS logPass (id INTEGER UNIQUE,login	TEXT NOT NULL,password TEXT NOT NULL,PRIMARY KEY(id AUTOINCREMENT));")
connectLogPass.commit()
cursorLogPass.execute("INSERT OR REPLACE INTO logPass VALUES(1, \"asd\",\"asd\")")
connectLogPass.commit()
mainWindow = MainWindow()
mainWindow.withdraw()

def AcceptLogPass():
    connectLogPass = sqlite3.connect("LogPass.db")
    query = 'SELECT * FROM logPass WHERE login = ? AND password = ?'
    LogPassBool = False

    if cursorLogPass.execute(query, (EntryLog.get(), EntryPass.get())).fetchone() != None:
        LogPassBool = True
    connectLogPass.commit()

    if LogPassBool:
        print("nice")
        #mainWindow.tableViewInsert()
        mainWindow.deiconify()
        LogPassWindow.destroy()


    else:
        print("not nice")

        showwarning(title="Неверный логин или пароль", message="Неверный логин или пароль, попробуйте снова")

if not os.path.exists("Projects"):
    os.makedirs("Projects")

LogPassWindow = Tk()
LogPassWindow.title("ProgramPython - Log in")
LogPassWindow.geometry("600x400")

MainLabel = ttk.Label(LogPassWindow,width=30, font=("Arial", 25),text="\"ООО\" ТЕРРИТОРИЯ КОМФОРТА",background="#ccff33")
MainLabel.pack(anchor=CENTER, pady=20)

EntryLog = ttk.Entry(LogPassWindow,width=15, font=("Arial", 20),background="#ccff33")
EntryLog.insert(0, "Login")
EntryLog.pack(anchor=CENTER, pady=20)

EntryPass = ttk.Entry(LogPassWindow,width=15, font=("Arial", 20),background="#ccff33")
EntryPass.config(show="*")
EntryPass.insert(0, "Password")
EntryPass.pack(anchor=CENTER)

BTLogPassAccept = ttk.Button(LogPassWindow, text="Log in", width=20, command=AcceptLogPass)
BTLogPassAccept.pack(anchor=CENTER)

Tables = ["Председатель клуба", "Организатор"]
Tables_var = StringVar(value=Tables[0])
comboBox = ttk.Combobox(LogPassWindow, textvariable=Tables_var, values=Tables, state="readonly")
comboBox.pack(anchor=NW, padx=6, pady=6)
comboBox.set("Организатор")

LogPassWindow.config(bg='#ccff33')
