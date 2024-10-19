import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-10, 10, 4000)
y_positive = np.sqrt(x1**2 - 1)
y_negative = -np.sqrt(x1**2 - 1)

x2 = np.linspace(-10, 10, 4000)
y2 = 1 / (1 - 2**(x2 / (1 - x2)))

fig, ax1 = plt.subplots()

ax1.plot(x1, y_positive, label='y = +√(x² - 1)', color='blue')
ax1.plot(x1, y_negative, label='y = -√(x² - 1)', color='blue')
ax1.set_xlabel('x')
ax1.set_ylabel('y = ±√(x² - 1)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(x2, y2, label='y = 1/(1 - 2^(x/(1-x)))', color='green')
ax2.set_ylabel('y = 1/(1 - 2^(x/(1-x)))', color='green')
ax2.tick_params(axis='y', labelcolor='green')

plt.title('Две функции с разными диапазонами')
fig.tight_layout()
plt.show()
