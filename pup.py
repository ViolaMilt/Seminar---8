import csv

with open(r"C:\Users\Вера\Desktop\Разработчик учеба\Python\Снеминар 8\CSV - файлы\Pup_list.csv") as ucheniki:
    file_reader_1 = csv.reader(ucheniki, delimiter=",")

    for row in file_reader_1:
      print(row)
