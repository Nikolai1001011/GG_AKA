import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Generate data
t = np.linspace(0, 2*np.pi, 100)
x = np.sin(t)
y = np.cos(t)
z = t

# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot initial point
point, = ax.plot([x[0]], [y[0]], [z[0]], marker='o', color='r')

# Update function
def update(frame):
    point.set_data(x[frame], y[frame])
    point.set_3d_properties(z[frame])
    return point,

# Animation
ani = FuncAnimation(fig, update, frames=len(t), blit=True)

plt.show()
