import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import main


x = []
y = []

figure, ax = plt.subplots(figsize=(4,3))
line, = ax.plot(x, y)
plt.axis([0, 4*np.pi, -1, 1])

volumen = main.dejar_salir.volumen

def func_animate(volumen):
    x = np.linspace(0, 4*np.pi, 1000)
    y = np.sin(2 * (x - 0.1 * volumen))
    
    line.set_data(x, y)
    
    return line,

ani = FuncAnimation(figure,
                    func_animate,
                    frames=10,
                    interval=50)

ani.save(r'animation.gif', fps=10)

plt.show()