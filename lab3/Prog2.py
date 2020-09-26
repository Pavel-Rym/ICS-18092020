import fractions

print("Калькулятор на Python. (!!!)Лише цілі числа(!!!)")
n1 = int(input('Введіть перше число: '))
n2 = int(input('Введіть друге число: '))
operation = int(input('Яку операцію робимо? 1 Додавання 2 Віднімання 3 Множення 4 Ділення'))

if operation == 1:
    r = n1 + n2
elif operation == 2:
    r = n1 - n2
elif operation == 3:
    r = n1 * n2
elif operation == 4:
    r = n1 / n2
else:
    r = 'Введено неправильну дію!'

if operation == 1:
   print('Отримуємо число', r)
elif operation == 2:
    print('Отримуємо число', r)
elif operation == 3:
    print('Отримуємо число', r)
elif operation == 4:
    print('Отримуємо число', r)

else:
    print (r)

        

