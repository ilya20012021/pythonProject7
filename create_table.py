import pandas as pd
from tabulate import tabulate

def ct():
    df = pd.DataFrame({})
    k = int(input("Введите кол-во значений:"))
    a = ["текст","число"]
    r = "/".join(a)
    print(f"Выберете тип данных столбца {r} :")
    s = str(input())
    if(s == "текст"):
        c = []
        for i in range(k):
            ccp = str(input("Введите значение:"))
            c.append(ccp)
        cc = str(input("Введите имя столбца:"))
        df[cc] = c
    elif (s == "число"):
        c = []
        for i in range(k):
            ccp = int(input("Введите значение:"))
            c.append(ccp)
        cc = str(input("Введите имя столбца:"))
        df[cc] = c
    else:
        exit("Попробуйте еще раз!")

    res = ["да","нет"]
    res_n = "/".join(res)
    print(f"Нужно ли добавить еще столбцы {res_n} :")
    s1 = str(input())
    if(s1 == "да"):
        n = int(input("Введите кол-во столбцов:"))
        for i in range(n):
            a = ["текст", "число"]
            r = "/".join(a)
            print(f"Выберете тип данных столбца {r} :")
            s = str(input())
            if (s == "текст"):
                c = []
                for i in range(k):
                    ccp = str(input("Введите значение:"))
                    c.append(ccp)
                cc = str(input("Введите имя столбца:"))
                df[cc] = c
            elif (s == "число"):
                c = []
                for i in range(k):
                    ccp = int(input("Введите значение:"))
                    c.append(ccp)
                cc = str(input("Введите имя столбца:"))
                df[cc] = c
            else:
                exit("Попробуйте еще раз!")
        print(tabulate(df, headers="keys", tablefmt="psql"))
        x = str(input("Введите имя таблицы:"))
        df.to_csv(f"{x}.csv")
        with open("1.txt", "a+") as f:
            f.write(f'{x} \n')
    elif(s1 == "нет"):
        print(tabulate(df,headers="keys",tablefmt="psql"))
        x = str(input("Введите имя таблицы:"))
        df.to_csv(f"{x}.csv")
        with open("1.txt", "a+") as f:
            f.write(f'{x}\n')

    else:
        exit("Попробуйте еще раз!")