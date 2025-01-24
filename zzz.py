import sqlite3

connect = sqlite3.connect("festival.db", timeout=5.0, detect_types=0,
                                           isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                           cached_statements=128, uri=False)
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Кошки (id INTEGER NOT NULL UNIQUE, Кличка TEXT, Порода TEXT, Возраст INTEGER, Клуб TEXT, Дата_последней_прививки TEXT, ФИО_хозяина TEXT, Номер_Документа INTEGER, Клички_родителей TEXT, PRIMARY KEY(id AUTOINCREMENT));")
connect.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Клубы (id INTEGER NOT NULL UNIQUE, Название_клуба TEXT, Породы_в_клубе TEXT, Количество_кошек INTEGER, Количество_экспертов INTEGER,  Количество_медалей INTEGER, названия_медалей TEXT, PRIMARY KEY(id AUTOINCREMENT));")
connect.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Эксперты (id INTEGER NOT NULL UNIQUE, Фамилия TEXT, Имя TEXT, Специализация_по_породе TEXT, Номер_ринга INTEGER, Клуб TEXT, PRIMARY KEY(id AUTOINCREMENT));")
connect.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Ринги (id INTEGER NOT NULL UNIQUE, Специализация_по_породе TEXT, id_обслуживающих_экспертов TEXT, PRIMARY KEY(id AUTOINCREMENT));")
connect.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Расписание (id INTEGER NOT NULL UNIQUE, id_ринга TEXT, Время TEXT, PRIMARY KEY(id AUTOINCREMENT));")
connect.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Результаты (id INTEGER NOT NULL UNIQUE, id_кошки TEXT, Очки INTEGER, Место INTEGER, PRIMARY KEY(id AUTOINCREMENT));")
connect.commit()