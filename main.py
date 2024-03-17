import matplotlib.pyplot as plt
import numpy as np

def sierpinski_triangle(ax, vertices, depth):
    if depth == 0:
        ax.fill(vertices[:, 0], vertices[:, 1], 'r')
    else:
        v0, v1, v2 = vertices
        midpoints = [(v0 + v1) / 2, (v1 + v2) / 2, (v2 + v0) / 2]
        sierpinski_triangle(ax, np.array([v0, midpoints[0], midpoints[2]]), depth - 1)
        sierpinski_triangle(ax, np.array([midpoints[0], v1, midpoints[1]]), depth - 1)
        sierpinski_triangle(ax, np.array([midpoints[2], midpoints[1], v2]), depth - 1)

# Create a new figure
fig, ax = plt.subplots()

# Define the vertices of an equilateral triangle
vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])

# Plot the Sierpinski triangle
sierpinski_triangle(ax, vertices, 5)

# Set aspect ratio to equal and turn off axes
ax.set_aspect('equal')
ax.axis('off')

# Show plot
plt.show()


