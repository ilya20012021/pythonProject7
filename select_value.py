import pandas as pd
from tabulate import tabulate

def value():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print(i)
    h = str(input("Введите название таблицы для работы:"))
    if (h in u):
        df = pd.read_csv(f"{h}.csv")
        print(tabulate(df,headers="keys",tablefmt="psql"))
        d = list(df.keys())
        dd = str(input("Введите столбец для дальнейшей работы:"))
        if (dd in d):
            sign = str(input("Введите знак:"))
            if(sign == "=="):
                v = str(input("Введите тип значения:"))
                if(v == "число"):
                    vv = int(input("Введите значение:"))
                    fin = df[df[dd] == vv]
                    print(tabulate(fin,headers="keys",tablefmt="psql"))
                    x = str(input("Введите имя таблицы:"))
                    fin.to_csv(f"{x}.csv")
                    with open("1.txt", "a+") as f:
                        f.write(f'{x}\n')
                elif(v == "текст"):
                    vv = str(input("Введите значение:"))
                    fin = df[df[dd] == vv]
                    print(tabulate(fin, headers="keys", tablefmt="psql"))
                    x = str(input("Введите имя таблицы:"))
                    fin.to_csv(f"{x}.csv")
                    with open("1.txt", "a+") as f:
                        f.write(f'{x}\n')
                else:
                    exit("Ошибка! Попробуйте еще раз!")
            elif (sign == ">="):
                v = str(input("Введите тип значения:"))
                if (v == "число"):
                    vv = int(input("Введите значение:"))
                    fin = df[df[dd] >= vv]
                    print(tabulate(fin, headers="keys", tablefmt="psql"))
                    x = str(input("Введите имя таблицы:"))
                    fin.to_csv(f"{x}.csv")
                    with open("1.txt", "a+") as f:
                        f.write(f'{x}\n')
                else:
                    exit("Ошибка! Попробуйте еще раз!")
            elif (sign == "<="):
                v = str(input("Введите тип значения:"))
                if (v == "число"):
                    vv = int(input("Введите значение:"))
                    fin = df[df[dd] <= vv]
                    print(tabulate(fin, headers="keys", tablefmt="psql"))
                    x = str(input("Введите имя таблицы:"))
                    fin.to_csv(f"{x}.csv")
                    with open("1.txt", "a+") as f:
                        f.write(f'{x}\n')
                else:
                    exit("Ошибка! Попробуйте еще раз!")
            elif (sign == "<"):
                v = str(input("Введите тип значения:"))
                if (v == "число"):
                    vv = int(input("Введите значение:"))
                    fin = df[df[dd] < vv]
                    print(tabulate(fin, headers="keys", tablefmt="psql"))
                    x = str(input("Введите имя таблицы:"))
                    fin.to_csv(f"{x}.csv")
                    with open("1.txt", "a+") as f:
                        f.write(f'{x}\n')
                else:
                    exit("Ошибка! Попробуйте еще раз!")
            elif (sign == ">"):
                v = str(input("Введите тип значения:"))
                if (v == "число"):
                    vv = int(input("Введите значение:"))
                    fin = df[df[dd] > vv]
                    print(tabulate(fin, headers="keys", tablefmt="psql"))
                    x = str(input("Введите имя таблицы:"))
                    fin.to_csv(f"{x}.csv")
                    with open("1.txt", "a+") as f:
                        f.write(f'{x}\n')
                else:
                    exit("Ошибка! Попробуйте еще раз!")
            else:
                exit("Ошибка! Попробуйте еще раз!")
        else:
            exit("Ошибка! Попробуйте еще раз!")
    else:
        exit("Ошибка! Попробуйте еще раз!")