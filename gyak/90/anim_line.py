import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ten_pi = np.pi * 10
x_vals = np.arange(0.0, ten_pi, 0.001)
y_vals = np.sin(x_vals)
plt.ylim([-5, 5])
plt.xticks([])
plt.yticks([])
ax.axis('off')

line, = plt.plot(x_vals, color="#c2185b", linewidth = 6)

def animate_line(i):
    if i > 10:
        i = 20 - i
    new_val = i / 5 * np.sin(x_vals)
    line.set_ydata(new_val)
    return [line]

myAnimation = animation.FuncAnimation(fig, animate_line, 20, blit=True)

"""
# loopolt gif
from matplotlib.animation import PillowWriter

class LoopingPillowWriter(PillowWriter):
    def finish(self):
        self._frames[0].save(
            self._outfile, save_all=True, append_images=self._frames[1:],
            duration=int(1000 / self.fps), loop=0)


myAnimation.save("line.gif", writer=LoopingPillowWriter(fps=24))
"""

plt.show()