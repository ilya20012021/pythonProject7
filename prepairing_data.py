import pandas as pd
from tabulate import tabulate

def clean():
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
        dd = []
        for i in d:
            a = str(input("Введите столбец для удаления:"))
            if(a in d):
                dd.append(a)
            elif(a == "стоп"):
                break
            else:
                exit("Ошибка! Попробуйте еще раз!")
        df.drop(columns=dd,inplace=True)
        print(tabulate(df, headers="keys", tablefmt="psql"))
        x = str(input("Введите имя таблицы:"))
        df.to_csv(f"{x}.csv")
        with open("1.txt", "a+") as f:
            f.write(f'{x}\n')
    else:
        exit("Ошибка! Попробуйте еще раз!")