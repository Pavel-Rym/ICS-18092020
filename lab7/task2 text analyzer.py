from collections import Counter
import pylab


str = "There are different kinds of animals on our planet, and all of them are very important for it"
counter = Counter(str)
pylab.title("Аналіз кількості букв у тексті")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] 
y = [counter['a'], counter['b'], counter['c'], counter['d'], counter['e'], counter['f'], counter['g'], counter['h'], counter['i'], counter['j'], counter['k'], counter['l'], counter['m'], counter['n'], counter['o'], counter['p'], counter['q'], counter['r'], counter['s'], counter['t'], counter['u'], counter['v'], counter['w'], counter['x'], counter['y'], counter['z']] 
pylab.bar (x, y, label = "Номер по x - порядковий номер в алфавіті") 
pylab.legend()
pylab.show() 