from data.data import quarter1_1
from data.data import quarter1_6
from data.data import quarter1_7
from data.data import quarter2_1
from data.data import quarter2_6
from data.data import quarter2_7
from data.data import quarter3_1
from data.data import quarter3_6
from data.data import quarter3_7
from data.data import quarter4_1
from data.data import quarter4_6
from data.data import quarter4_7
from data.data import notes
import json
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np

def printtable(somelist):
  for t1 in somelist:
     print (t1)


start = int(input("Що робимо? \n 1 - Зробити аналіз товарообігу \n 2 - Вивести вхідні дані")) 

if start == 1:

  notes = """ {
    "1": "Універсам №1",
    "6": "Галактон",
    "7": "Поляниця"
  } """
  data = json.loads(notes)
  
  def percents(a, b):
    return b / a * 100
    
  def eff(a, b):
    return a / b

  table = PrettyTable(["Назва магазину", "Квартал", "Плановий товарообіг", "Фактичний товарообіг", "Вітсотки виконання", "Планова продуктивність", "Фактична продуктивність"])
  result_shops = [data["1"], data["1"], data["1"], data["1"], data["6"], data["6"], data["6"], data["6"], data["7"], data["7"], data["7"], data["7"]]
  result_quarter = [quarter1_1[0], quarter2_1[0], quarter3_1[0], quarter4_1[0], quarter1_6[0], quarter2_6[0], quarter3_6[0], quarter4_6[0], quarter1_7[0], quarter2_7[0], quarter3_7[0], quarter4_7[0]]
  result_stuff_plan = [quarter1_1[2], quarter2_1[2], quarter3_1[2], quarter4_1[2], quarter1_6[2], quarter2_6[2], quarter3_6[2], quarter4_6[2], quarter1_7[2], quarter2_7[2], quarter3_7[2], quarter4_7[2]]
  result_stuff_fact = [quarter1_1[3], quarter2_1[3], quarter3_1[3], quarter4_1[3], quarter1_6[3], quarter2_6[3], quarter3_6[3], quarter4_6[3], quarter1_7[3], quarter2_7[3], quarter3_7[3], quarter4_7[3]]
  result_stuff_percents = ["%.2f" % percents(quarter1_1[2], quarter1_1[3]), "%.2f" % percents(quarter2_1[2], quarter2_1[3]), "%.2f" % percents(quarter3_1[2], quarter3_1[3]), "%.2f" % percents(quarter4_1[2], quarter4_1[3]), "%.2f" % percents(quarter1_6[2], quarter1_6[3]), "%.2f" % percents(quarter2_6[2], quarter2_6[3]), "%.2f" % percents(quarter3_6[2], quarter3_6[3]), "%.2f" % percents(quarter4_6[2], quarter4_6[3]), "%.2f" % percents(quarter1_7[2], quarter1_7[3]), "%.2f" % percents(quarter2_7[2], quarter2_7[3]), "%.2f" % percents(quarter3_7[2], quarter3_7[3]), "%.2f" % percents(quarter4_7[2], quarter4_7[3]),]
  result_eff_plan = ["%.2f" % eff(quarter1_1[2], quarter1_1[4]), "%.2f" % eff(quarter2_1[2], quarter2_1[4]), "%.2f" % eff(quarter3_1[2], quarter3_1[4]), "%.2f" % eff(quarter4_1[2], quarter4_1[4]), "%.2f" % eff(quarter1_6[2], quarter1_6[4]), "%.2f" % eff(quarter2_6[2], quarter2_6[4]), "%.2f" % eff(quarter3_6[2], quarter3_6[4]), "%.2f" % eff(quarter4_6[2], quarter4_6[4]), "%.2f" % eff(quarter1_7[2], quarter1_7[4]), "%.2f" % eff(quarter2_7[2], quarter2_7[4]), "%.2f" % eff(quarter3_7[2], quarter3_7[4]), "%.2f" % eff(quarter4_7[2], quarter4_7[4])]
  result_eff_fact = ["%.2f" % eff(quarter1_1[3], quarter1_1[5]), "%.2f" % eff(quarter2_1[3], quarter2_1[5]), "%.2f" % eff(quarter3_1[3], quarter3_1[5]), "%.2f" % eff(quarter4_1[3], quarter4_1[5]), "%.2f" % eff(quarter1_6[3], quarter1_6[5]), "%.2f" % eff(quarter2_6[3], quarter2_6[5]), "%.2f" % eff(quarter3_6[3], quarter3_6[5]), "%.2f" % eff(quarter4_6[3], quarter4_6[5]), "%.2f" % eff(quarter1_7[3], quarter1_7[5]), "%.2f" % eff(quarter2_7[3], quarter2_7[5]), "%.2f" % eff(quarter3_7[3], quarter3_7[5]), "%.2f" % eff(quarter4_7[3], quarter4_7[5])] 

  for x in range(0, 12):
    table.add_row([result_shops[x], result_quarter[x], result_stuff_plan[x], result_stuff_fact[x], result_stuff_percents[x], result_eff_plan[x], result_eff_fact[x]])

  print(table)

  shedule = int(input("Якщо бажаєте побачити графік продуктивності, введіть 1"))
  if shedule == 1:
    x = [1, 2, 3, 4]
    y1p = [206, 263, 345, 342]
    y1f = [235, 272, 350, 358]
    y2p = [260, 345, 316, 313]
    y2f = [273, 355, 325, 308]
    y3p = [274, 275, 315, 265]
    y3f = [313, 304, 317, 267]
    plt.plot(x, y1p, '--r', x, y1f, '-r', x, y2p, '--b', x, y2f, '-b', x, y3p, '--g', x, y3f, '-g')
    plt.show()
    print('Червона лінія - "Універсам №1, синя - "Галактон", зелена - "Поляниця. \n Пунктирна лінія - планова продуктивність, суцільна - фактична')



  else:
    pass
  

elif start == 2:
  input_data = int(input("Які саме вхідні дані вивести? \n 1 - Вивести вхідні дані за 1 квартал \n 2 - Вивести вхідні дані за 2 квартал \n 3 - Вивести вхідні дані за 3 квартал \n 4 - Вивести вхідні дані за 4 квартал \n 5 - Вивести довідник \n 6 - Вивести всі вхідні дані"))
  if input_data == 1:
    print("Показники діяльності підприємств об'єднання 'Столичний' \n | Квартал | Номер магазина | Товарообіг(плановий/фактичний) | Чисельність,чол(планова/фактична) |")
    print(quarter1_1) 
    print(quarter1_6) 
    print(quarter1_7) 
  elif input_data == 2:
    print("Показники діяльності підприємств об'єднання 'Столичний' \n | Квартал | Номер магазина | Товарообіг(плановий/фактичний) | Чисельність,чол(планова/фактична) |")
    print(quarter2_1) 
    print(quarter2_6) 
    print(quarter2_7) 
  elif input_data == 3:
    print("Показники діяльності підприємств об'єднання 'Столичний' \n | Квартал | Номер магазина | Товарообіг(плановий/фактичний) | Чисельність,чол(планова/фактична) |")
    print(quarter3_1) 
    print(quarter3_6) 
    print(quarter3_7) 
  elif input_data == 4:
    print("Показники діяльності підприємств об'єднання 'Столичний' \n | Квартал | Номер магазина | Товарообіг(плановий/фактичний) | Чисельність,чол(планова/фактична) |")
    print(quarter4_1) 
    print(quarter4_6) 
    print(quarter4_7) 
  elif input_data == 5:
    print("Довідник магазинів")
    printtable(notes)
  elif input_data == 6:
    print("Показники діяльності підприємств об'єднання 'Столичний' \n | Квартал | Номер магазина | Товарообіг(плановий/фактичний) | Чисельність,чол(планова/фактична) |")
    print(quarter1_1) 
    print(quarter1_6) 
    print(quarter1_7) 
    print(quarter2_1) 
    print(quarter2_6) 
    print(quarter2_7) 
    print(quarter3_1) 
    print(quarter3_6) 
    print(quarter3_7) 
    print(quarter4_1) 
    print(quarter4_6) 
    print(quarter4_7) 
    print("Довідник магазинів")
    printtable(notes)
  else:
    print("Невірно введений запит")
else:
    print("Невірно введений запит")


input('Press ENTER to exit') 

  





