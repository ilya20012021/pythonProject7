import pandas as pd
from tabulate import tabulate

def read():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print(i)
    h = str(input("Введите название таблицы для работы:"))
    if (h in u):
        df = pd.read_csv(f"{h}.csv")
        print(tabulate(df,headers="keys",tablefmt="psql"))
    else:
        exit("Такой таблицы нет!")