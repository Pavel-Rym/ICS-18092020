class Dictionary():
   words={'word': 'світ',\
    'earth':'земля',\
    'you': 'ти',\
    'I':'я',\
    'We':'ми',\
    'probably':'напевно',\
    'piece':'кусок',\
    'tired':'втомлений',\
    'should':'повинен',\
    'be able':'быть в состоянии',\
    'not enough':'не хватает',\
    'enough':'достаточно',\
    'should':'повинен',\
    'represent':'представляти',\
    'sequence':'послідовність'}


 def eng():
    eng_words=dict([[v, k] for k,v in words.items()])
    find_word=input('Enter word ' '')
    print(eng_words.get(find_word) or print('No such key'))

 def rus():
    key=input('Введіть слово ' '')
    print (words.get(key) or 'Слово не знайдено')

 if __name__ == '__main__':
    x=input('Знайти перевод англійского слова? ' '')
    if x == 'y':
        rus()
    elif x == 'n':
        eng()
    else:
        print('Роботу завершено')

        