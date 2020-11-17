class Student():
    name = str(input("Ведіть ім'я студента"))
    mark_lab = int(input("Введіть бал студента за лабораторну роботу"))
    mark_indiv = int(input("Введіть бал студента за творче завдання"))
    max_mark_lab = 10
    max_mark_indiv = 30
    auto_mark = 92


    def __init__(self, name):
        self.name = name
    d = dict("max_mark_lab": 10, "max_mark_indiv": 30, "max_lab": 7, "max_mark": 100, "auto_mark": 0.92)

    if mark_lab > max_mark_lab:
        print("Невірно введена оцінка за лабораторну роботу")

    else:
        pass

    if mark_indiv > max_mark_indiv:
        print("Невірно введена оцінка за індивідуальне завдання")
    
    else:
        pass

    lab_attemps = int(input("Кількість спроб здати лабораторну роботу"))
    lab_last_mark = int(input("Остання оцінка за лабораторну роботу"))
    
    def lab(self, lab_attemps, lab_last_mark): 
        self.lab_attemps = lab_attemps
        self.lab_last_mark = lab_last_mark
    print("Лабораторна, кількість спроб та остання оцінка:" + str(lab_attemps) + "," + str(lab_last_mark))

    indiv_attemps = int(input("Кількість спроб здати індивідуальне завдання"))
    indiv_last_mark = int(input("Остання оцінка за індивідуальне завдання"))

    def indiv(self, indiv_attemps, indiv_last_mark): 
        self.indiv_attemps = indiv_attemps
        self.indiv_last_mark = indiv_last_mark
    print("Індивідуальне завдання, кількість спроб та остання оцінка:" + str(indiv_attemps) + "," + str(indiv_last_mark))

    def auto_f(self, mark_lab, mark_indiv):
        return mark_lab + mark_indiv
    if auto_f => auto_mark:
        auto = True
    else:
        auto = False 

    
    






    
     