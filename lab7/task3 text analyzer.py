from collections import Counter
import pylab


str = "Would you like a drink, sir?	Yes, a Diet Coke, please.	Ice and lemon. Just lemon.	Here you are.Thank you.Coffee? Tea?Coffee, please.	Milk? Yes, please!	Sugar?No, thanks!Here you are... Thanks!"
counter = Counter(str)
pylab.title("Типи речення у тексті")
x = [1, 2, 3, 4] 
y1 = counter['.']
y2 = counter['?']
y3 = counter['!']
y4 = counter['...']
pylab.bar (x[0], y1, label ="Звичайні") 
pylab.bar (x[1], y2, label = "Питальні", color = "red")
pylab.bar(x[2], y3, label = "Окличні", color = "green")
pylab.bar(x[3], y4, label = "Три крапки", color = "black")
pylab.legend()
pylab.show() 