import csv

with open(r"C:\Users\Вера\Desktop\Разработчик учеба\Python\Снеминар 8\CSV - файлы\family.csv") as roditeli:
    file_reader_2 = csv.DictReader(roditeli, delimiter=",")

    for row in file_reader_2:
          print(row)
