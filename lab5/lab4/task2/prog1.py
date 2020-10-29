infile = open("D:\\Study\\ICS-18.09.2020\\lab5\\lab4\\task2\\Intermezzo.txt", 'r')
characters = 0
words = 0
for line in infile:
    wordslist = line.split()
    words = words + len(wordslist)
    characters = characters + len(line)
print(characters, "букв") 
print(words, "слів")