import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

def lines():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print(i)
    h = str(input("Введите название таблицы для работы:"))
    if (h in u):
        df = pd.read_csv(f"{h}.csv")
        print(tabulate(df, headers="keys", tablefmt="psql"))
        d = list(df.keys())
        dd = str(input("Введите столбец для дальнейшей работы:"))
        if (dd in d):
            m = list(df[dd])
            plt.hist(m,bins=10)
            plt.show()
    else:
        exit("Ошибка! Попробуйте еще раз!")