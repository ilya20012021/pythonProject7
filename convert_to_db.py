import sqlite3 as sq
import pandas as pd

def data():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print(i)
    h = str(input("Введите название таблицы для работы:"))
    if (h in u):
        df = pd.read_csv(f"{h}.csv")
        connection = sq.connect(f'{h}.db')
        name_db = str(input("Введите имя табл:"))
        df.to_sql(name_db, connection, if_exists='replace', index=False)
        connection.close()
    else:
        exit("Ошибка! Попробуйте еще раз!")