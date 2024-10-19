import matplotlib.pyplot as plt  
import numpy as np  

x = np.linspace(-10, 10, 4000)
y_positive = np.sqrt(x**2 - 1)
y_negative = -np.sqrt(x**2 - 1)

plt.plot(x, y_positive, x, y_negative)  
plt.title('График функции y = ±√(x² - 1)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()  
