import csv
import user

a = "класс"
b = "ФИО родителя"
c = "телефон"

e = user.fio
z = user.zapros
q = " "
id = " "
fio = " "
klass = " "
otvet = " "

with open(r"C:\Users\Вера\Desktop\Разработчик учеба\Python\Снеминар 8\CSV - файлы\Pup_list.csv") as ucheniki:
    file_reader_1 = csv.reader(ucheniki, delimiter=",")
    for stroka in file_reader_1:
      for j in stroka:
        if stroka[1] == e:
           otvet = "да"

if otvet != "да":
    print("Такого ученика не найдено")

def Poisk_id():
    with open(r"C:\Users\Вера\Desktop\Разработчик учеба\Python\Снеминар 8\CSV - файлы\Pup_list.csv") as ucheniki:
        file_reader_1 = csv.reader(ucheniki, delimiter=",")
        for row in file_reader_1:
            for i in row:
                if row[1] == e:
                    id = row[0]
    return id




def Klass():
    with open(r"C:\Users\Вера\Desktop\Разработчик учеба\Python\Снеминар 8\CSV - файлы\Pup_list.csv") as ucheniki:
        file_reader_1 = csv.reader(ucheniki, delimiter=",")
        for row in file_reader_1:
            for i in row:
                if row[1] == e:
                    klass = row[3]
        print(klass)
    return klass

def Poisk_fio(id):
   with open(r"C:\Users\Вера\Desktop\Разработчик учеба\Python\Снеминар 8\CSV - файлы\family.csv") as family:
        file_reader_2 = csv.reader(family, delimiter=",")
        fio = " "
        for line in file_reader_2:
            for j in line:
                if line[0] == id:
                    fio = line[1],line[2],line[3]
        print(fio)
   return fio


def Poisk_tel(id):
   with open(r"C:\Users\Вера\Desktop\Разработчик учеба\Python\Снеминар 8\CSV - файлы\family.csv") as family:
        file_reader_2 = csv.reader(family, delimiter=",")
        telefon = " "
        for line in file_reader_2:
            for j in line:
                if line[0] == id:
                    telefon = line[4]
        print(telefon)
   return telefon

cur_id = Poisk_id()
if z == a:
    Klass()

if z == b:
     Poisk_id()
     Poisk_fio(cur_id)

if z == c:
    Poisk_id()
    Poisk_tel(cur_id)



