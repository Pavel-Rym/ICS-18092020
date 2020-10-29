from pathlib import Path
import os 
import csv

os.chdir("D:\\Study\\ICS-18.09.2020\\lab5\\lab4\\task2")

book = "D:\\Study\\ICS-18.09.2020\\lab5\\lab4\\task2\\Intermezzo.txt"

def numberOfDifferentWords():
    a = len(set(Path(book).read_text(encoding = "utf-8").split()))
    s = set(Path(book).read.txt(encoding = "utf-8"))
    n = 0
    for symbol in s:
        if symbol == "—":
            n = 1
    print("number of different words: " + str(a-n))

def numberOfUniqueWords():
    unique_words = set()
    worldlist = Path(book).read_text(encoding = "utf-8").split()
    for i in range (0, len(wordlist)):
        if(wordlist.count(wordlist[i]) == 1):
            unique_words.add(wordlist[i])
    print("number of unique words: " + str(len(unique_words)))

