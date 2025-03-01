import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo, askyesno
import sv_ttk
from MainWindowClubAdmin import MainWindowClubAdmin
from MainWindowOrganisator import *
import sqlite3
import random
import sys


connectLogPass = sqlite3.connect("LogPass.db")
cursorLogPass = connectLogPass.cursor()
cursorLogPass.execute("CREATE TABLE IF NOT EXISTS logPass (id INTEGER UNIQUE,login	TEXT NOT NULL,password TEXT NOT NULL,PRIMARY KEY(id AUTOINCREMENT));")
connectLogPass.commit()
cursorLogPass.execute("INSERT OR REPLACE INTO logPass VALUES(1, \"asd\",\"asd\")")
connectLogPass.commit()
mainWindow = MainWindowOrganisator()
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
        if comboBox.get() == "Организатор":

            #mainWindow.tableViewInsert()
            mainWindow.deiconify()
            LogPassWindow.destroy()
        else:
            mainWindow.destroy()
            mainWindowSecond = MainWindowClubAdmin()
            LogPassWindow.destroy()


    else:
        print("not nice")

        showwarning(title="Неверный логин или пароль", message="Неверный логин или пароль, попробуйте снова")

if not os.path.exists("Projects"):
    os.makedirs("Projects")

LogPassWindow = Tk()
LogPassWindow.title("ProgramPython - Log in")
LogPassWindow.geometry("600x400")
sv_ttk.set_theme("dark", LogPassWindow)

def on_entry_click1( event):
    if EntryLog.get() == 'Login':
        EntryLog.delete(0, "end")
        EntryLog.insert(0, '')
        EntryLog.config(foreground='white')
def on_focusout1(event):
    if EntryLog.get() == '':
        EntryLog.insert(0, 'Login')
        EntryLog.config(foreground='grey')
def on_entry_click2( event):
    if EntryPass.get() == 'Password':
        EntryPass.delete(0, "end")
        EntryPass.insert(0, '')
        EntryPass.config(foreground='white')
def on_focusout2( event):
    if EntryPass.get() == '':
        EntryPass.insert(0, 'Password')
        EntryPass.config(foreground='grey')

MainLabel = ttk.Label(LogPassWindow,width=30, font=("Arial", 30),text="          ВЫСТАВКА КОШЕК")
MainLabel.pack(anchor=CENTER, pady=20)

EntryLog = ttk.Entry(LogPassWindow, width=15, font=("Arial", 20), foreground='grey')
EntryLog.insert(0, "Login")
EntryLog.bind('<FocusIn>', on_entry_click1)
EntryLog.bind('<FocusOut>', on_focusout1)
EntryLog.pack(anchor=CENTER, pady=10)

EntryPass = ttk.Entry(LogPassWindow, width=15, font=("Arial", 20), foreground='grey')
EntryPass.config(show="*")
EntryPass.insert(0, "Password")
EntryPass.bind('<FocusIn>', on_entry_click2)
EntryPass.bind('<FocusOut>', on_focusout2)
EntryPass.pack(anchor=CENTER, pady=10)

BTLogPassAccept = ttk.Button(LogPassWindow, text="Log in", width=20, command=AcceptLogPass)
BTLogPassAccept.pack(anchor=CENTER)

Tables = ["Председатель клуба", "Организатор"]
Tables_var = StringVar(value=Tables[0])
comboBox = ttk.Combobox(LogPassWindow, textvariable=Tables_var, values=Tables, state="readonly")
comboBox.pack(anchor=NW, padx=6, pady=6)
comboBox.set("Организатор")


