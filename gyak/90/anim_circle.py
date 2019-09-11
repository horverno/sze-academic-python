import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
two_pi = np.pi * 2
x_vals = np.arange(0.0, two_pi, 0.001)
y_vals = np.sin(x_vals)
ax = plt.axis([0, two_pi, -1.1, 1.1])
moving_point, = plt.plot([0], [np.sin(0)], marker = 'o', markerfacecolor="#ffc819", markeredgecolor='w', markersize = 100)

def animate_point(i):
    moving_point.set_data(i, np.sin(i))
    return moving_point,

fr = np.arange(0.0, two_pi, 0.1)
myAnimation = animation.FuncAnimation(fig, animate_point, frames=fr, repeat=True, blit=True, interval=10)
# from matplotlib.animation import PillowWriter
# myAnimation.save("circle.gif", writer=PillowWriter(fps=24))
plt.show()