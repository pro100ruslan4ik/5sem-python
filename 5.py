import numpy as np
import matplotlib.pyplot as plt

from sympy import symbols, diff, lambdify

x, y = symbols('x y')

z = 2*x**2 + 6*x*y + 2*y**2 + 2*x - 2*y + 3

z_x = diff(z, x)
z_y = diff(z, y)

z_x_func = lambdify((x, y), z_x, 'numpy')
z_y_func = lambdify((x, y), z_y, 'numpy')

X, Y = np.meshgrid(np.linspace(-10, 10, 10), np.linspace(-10, 10, 10))

U = z_x_func(X, Y)  
V = z_y_func(X, Y)  

fig = plt.figure(figsize=(7, 7))
ax1 = fig.add_subplot(121)
ax1.quiver(X, Y, U, V, color="b", angles="xy", scale_units="xy", scale=10)
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_title("Векторное поле")
ax1.grid(True)


ax2 = fig.add_subplot(122)
ax2.streamplot(X, Y, U, V, color="b", density=0.5)
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_title("Линии тока")
ax2.grid(True)
plt.show()
