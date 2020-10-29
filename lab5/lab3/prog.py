
#Читання файлу 

import os,sys,csv

filename = "D:\Study\ICS-18.09.2020\lab5\lab3\list1.txt"

fd = open(filename) 
reader = csv.reader(fd, delimiter="\t") 
for row in reader:     
    print(row) 
fd.close() 
    
#Запис даних у файл

filename = "D:\Study\ICS-18.09.2020\lab5\lab3\list1.txt"

fd = open(filename, "w") 
for i in range(10):     
    A = i*18     
    fd.write("%i\t%.1f\n" % (i, A)) 
fd.close() 

#Пошук файлів у каталозі 

for filename in os.listdir("..\\plugins"):     
    print(filename) 

#Пошук данних у файлі
from __future__ import print_function
import io

word = u'Шукане слово'
with io.open('D:\Study\ICS-18.09.2020\lab5\lab3\list1.txt', encoding='utf-8') as file:
    for line in file:
        if word in line:
            print(line, end='')

#Пошук файлів у каталозі

import os

for root, dirs, files in os.walk('D:\Study\ICS-18.09.2020\lab5\lab3\'):
        for file in files:
            if file.endswith(".csv"):
                path_file = os.path.join(root,file)
                print(path_file)


#Сортування за середнім балом 

with open("D:\Study\ICS-18.09.2020\lab5\lab3\list1.txt") as file:
    lines = file.readlines()
    lines.sort(key=lambda line: int(line.split(' -> ')[0]))

print(lines)