import os
 
filename = "D:\\Study\\ICS-18.09.2020\\lab5\\lab4\\task2\\Intermezzo.txt"

def get_words(filename):
 
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words
 
 
def get_words_dict(words):
    words_dict = dict()
 
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
 
 
def main():
    filename = "D:\\Study\\ICS-18.09.2020\\lab5\\lab4\\task2\\Intermezzo.txt"
    if not os.path.exists(filename):
        print()
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print("Кількість слів: %d" % len(words))
        print("Всі слова:")
        for word in words_dict:
             print(word.ljust(20), words_dict[word])
 
 
if __name__ == "__main__":
    main()