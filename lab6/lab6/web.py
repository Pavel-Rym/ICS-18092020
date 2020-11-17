import requests 
r = requests.get('https://api.github.com/events')  
r.text

def get_words(r):
 
    with open(r, encoding="utf8") as page:
        text = page.read()
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
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print("Кільість слів: %d" % len(words))
        print("Кількість тегів: %d" % len(words_dict))
        print("Кількість посилань:")
        for word in words_dict:
             print(word.ljust(20), words_dict[word])
 
 
if __name__ == "__main__":
    main()