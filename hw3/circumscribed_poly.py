import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

# Set up figure and axes
fig, ax = plt.subplots(figsize=(6, 6))

# Radius of the inscribed circle
r = 1.0

# Regular octagon parameters
n = 8
R = r / np.cos(np.pi / n)  # circumradius

# Compute vertices of the regular octagon (centered at origin)
angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
vertices = np.column_stack((R * np.cos(angles), R * np.sin(angles)))

# Draw the octagon (red excess area)
octagon = Polygon(vertices, closed=True,
                  facecolor='red', edgecolor='k', alpha=0.5,
                  label='Excess octagon area')
ax.add_patch(octagon)

# Draw the inscribed circle
circle = Circle((0, 0), r,
                facecolor='white', edgecolor='k', linewidth=1.5,
                label='Inscribed circle')
ax.add_patch(circle)

# Compute midpoints of each edge
midpoints = []
for i in range(n):
    p1 = vertices[i]
    p2 = vertices[(i + 1) % n]
    mid = 0.5 * (p1 + p2)
    midpoints.append(mid)
midpoints = np.array(midpoints)

# Draw dotted red lines connecting adjacent midpoints
for i in range(n):
    m1 = midpoints[i]
    m2 = midpoints[(i + 1) % n]
    ax.plot([m1[0], m2[0]], [m1[1], m2[1]],
            'r--', linewidth=1)

# --- Blue circumradius to the rightmost vertex ---
right_idx = np.argmax(vertices[:, 0])
right_vertex = vertices[right_idx]

ax.plot([0, right_vertex[0]], [0, right_vertex[1]],
        color='blue', linewidth=2, label='Circumradius')

# Add text label "circumradius" near the rightmost vertex
ax.text(right_vertex[0] + 0.1 * R, right_vertex[1],
        'circumradius', color='blue', fontsize=10,
        ha='left', va='center')

# --- Green inradius to the midpoint of a nearby edge ---
ax.plot([0, midpoints[-1][0]], [0, midpoints[-1][1]],
        color='green', linewidth=2, label='Inradius')

# Add text label "inradius" near the midpoint of that edge
ax.text(midpoints[-1][0] + 0.1 * R, midpoints[-1][1] + 0.05 * R,
        'inradius', color='green', fontsize=10,
        ha='left', va='center')

# Axes settings
ax.set_aspect('equal', 'box')
ax.set_xlim(-R * 1.2, R * 1.4)
ax.set_ylim(-R * 1.2, R * 1.4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Regular Octagon with Inscribed Circle\nRed = Excess Area, Blue = Circumradius R, Green = Inradius r')
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.show()