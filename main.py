import convert_to_db
import create_table
import histogram
import prepairing_data
import read_table
import select_value
import update_table

a = ["создать массив данных(нажмите 1)","обновить массив данных(нажмите 2)","считать все данные таблицы(нажмите 3)","выбрать данные по столбцу(нажмите 4)","подготовка данных(нажмите 5)","построить гистограмму(нажмите 6)","кинуть данные на сервер(нажмите 7)"]
for i in a:
    print(i)
s = str(input("Выберите функционал фреймворка:"))
if(s == "1"):
    create_table.ct()
elif(s == "2"):
    update_table.upd()
elif(s == "3"):
    read_table.read()
elif(s == "4"):
    select_value.value()
elif(s == "5"):
    prepairing_data.clean()
elif(s == "6"):
    histogram.lines()
elif(s == "7"):
    convert_to_db.data()
else:
    exit("Попробуйте еще раз!")