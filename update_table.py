import pandas as pd
from tabulate import tabulate

def upd():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print(i)
    h = str(input("Введите название таблицы для работы:"))
    if (h in u):
        df = pd.read_csv(f"{h}.csv")
        print(tabulate(df, headers="keys", tablefmt="psql"))
        print("-------------------------------------------")
        columns = df.keys()
        column = str(input("Введите столбец для обновления данных:"))
        if(column in columns):
            index = int(input("Введите номер строки:"))
            if(0 <= index < len(list(df[column]))):
                a = ["текст", "число"]
                r = "/".join(a)
                print(f"Выберете тип данных  {r} :")
                s = str(input())
                if (s == "текст"):
                    s1 = str(input("Введите значение:"))
                    df.at[index, column] = s1
                    print(tabulate(df, headers="keys", tablefmt="psql"))
                    x1 = str(input("Введите имя таблицы:"))
                    df.to_csv(f"{x1}.csv")
                    with open("1.txt", "a+") as f:
                        f.write(f'{x1}\n')
                elif (s == "число"):
                    s2 = int(input("Введите значение:"))
                    df.at[index, column] = s2
                    print(tabulate(df, headers="keys", tablefmt="psql"))
                    x2 = str(input("Введите имя таблицы:"))
                    df.to_csv(f"{x2}.csv")
                    with open("1.txt", "a+") as f:
                        f.write(f'{x2}\n')
                else:
                    exit("Попробуйте еще раз!")
            else:
                exit("Отсутствие данного номера строки!")
        else:
            exit("Попробуйте еще раз!")
    else:
        exit("Такой таблицы нет!")