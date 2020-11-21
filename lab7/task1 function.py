from numpy import * 
import matplotlib.pyplot as plt 

x = linspace(0, 7, 1000) 

y = 5*sin(10*x)*sin(3*x)/(x**(1/2))
plt.plot(x, y, label = "Y(x)=5*sin(10*x)*sin(3*x)/(x^(1/2))") 
plt.title("Графік функції")
plt.legend()
plt.savefig('zad1 function.png', dpi=200) 
plt.show() 

