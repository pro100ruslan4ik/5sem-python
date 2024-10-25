import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)  
r = 2 * (1 + np.cos(theta))

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.plot(theta, r, linewidth=2)

ax.set_title("График в полярных координатах", va='bottom')
plt.show()
