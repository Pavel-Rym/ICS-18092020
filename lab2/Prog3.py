print("Калькулятор на Python")
n1 = int (input('Введіть перше число: '))
n2 = int (input('Введіть друге число: '))
operation = int("Яку операцію робимо? 1 Додавання 2 Віднімання")

if operation == 1:
    r = n1 + n2
elif operation == 2:
    r = n1 - n2
else:
    r = "Помилка"

print('Отримуємо:', r)