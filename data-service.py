from data.data import table1
from data.data import table2

"""Імпорт данних з массиву"""

def printtable(somelist):
  for t1 in somelist:
     print (t1)

"""Структуризація данних з таблиць"""

print("Вхідні дані")
print("Квартал | Номер магазина | Товарообіг(плановий/фактичний) | Чисельність,чол(планова/фактична)")
printtable(table1)

"""Виведення першої таблиці"""

print("Довідник магазинів")
print("Номер магазина | Назва")
printtable(table2)

"""Виведення другої таблиці"""