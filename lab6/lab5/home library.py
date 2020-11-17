class Library(object):
    def __init__(self,
                 title="",
                 authors=[],
                 year=None):
        self.title = title
        self.authors = authors
        self.year = year
    def __str__(self):
        return str(self.__dict__)
 
books = [Library(b[0], b[1], b[2]) for b in [
    ("Війна та мир", ["Lev Tolstoy"], 1867),
    ("Гайдамаки", ["Taras Shevchenko"], 1841),
    ("Катерина", ["Taras Shevchenko"], 1975),
    ("Місто", ["Valerian Pidmohilniy"], 1928),
    ("Модри Камень", ["Oles Honchar"], 2018)
]]
 
print ("All Books:")
for b in books:
    print (b)
 
def select_by_year(books, year):
    for b in books:
        if b.year == year:
            yield b
 
print ("Books in 1867:")
for b in select_by_year(books, 1867):
    print (b)
 
print ("Books of Taras Shevchenko:")
for b in [b for b in books if "Taras Shevchenko" in b.authors]:
    print (b)
 
print ("Sorted books by title:")
for b in sorted(books, key=lambda b: b.title):
    print (b)
    