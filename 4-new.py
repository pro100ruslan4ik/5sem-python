import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

Z = 2*X**2 + 6*X*Y + 2*Y**2 + 2*X - 2*Y + 3

levels = [-40, -30, -20, -10, 0, 10, 20, 30, 40]
fig = plt.figure(figsize=(12, 8))

gs = gridspec.GridSpec(4, 4, figure=fig)

ax1 = fig.add_subplot(gs[0:2,0:2], projection='3d')

ax1.plot_surface(X, Y, Z, edgecolor='none', alpha=0.3)
ax1.contour(X, Y, Z, levels=[0], colors='red', linestyles="dashed", offset=0)

ax1.set_zlim(-10,10)
ax1.set_title("3D график поверхности z = [-10,10]")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

ax2 = fig.add_subplot(gs[2:4,0:2], projection='3d')

ax2.plot_surface(X,Y,Z, alpha=0.7)
ax2.contour(X,Y,Z, levels=[0], colors='red', linestyles="dashed", offset=0)

ax2.set_title("3D график поверхности")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")


ax3 = fig.add_subplot(gs[0:2,2:4])
contour = ax3.contour(X, Y, Z, levels=levels) 
plt.colorbar(contour, ax=ax3)

ax4 = fig.add_subplot(gs[2:4,2:4])
contour = ax4.contourf(X, Y, Z, levels=levels, linestyles="dashed") 
plt.colorbar(contour, ax=ax4)

plt.show()
