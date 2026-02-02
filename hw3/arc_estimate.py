import numpy as np
import matplotlib.pyplot as plt

# Function
f = lambda x: np.sin(np.pi/2 * x)

# Domain for smooth plot
x = np.linspace(0, 1, 400)
y = f(x)

# Number of rectangles
n = 4
a, b = 0, 1
dx = (b - a) / n

# Rectangle endpoints
x_edges = np.linspace(a, b, n + 1)

# Midpoints for tangent lines
x_mid = (x_edges[:-1] + x_edges[1:]) / 2
y_mid = f(x_mid)

plt.figure(figsize=(8, 5))

# Plot sin(pi/2 * x)
plt.plot(x, y, 'k', label={r'$\sin(\pi x / 2)$'})

# Plot step function rectangles (upper edges + vertical sides)
for i in range(n):
    x_left = x_edges[i]
    x_right = x_edges[i + 1]
    
    # Height at right end (right Riemann sum)
    h = f(x_right)
    
    # Horizontal top edge (thinner line)
    plt.plot(
        [x_left, x_right], [h, h],
        'r', linewidth=1,
        label='Rectangle approximation' if i == 0 else ""
    )
    # Left vertical side
    plt.plot([x_left, x_left], [0, h], 'r', linewidth=1)
    # Right vertical side
    plt.plot([x_right, x_right], [0, h], 'r', linewidth=1)

# Tangent lines at midpoints (thinner line)
for j, (xm, ym) in enumerate(zip(x_mid, y_mid)):
    # derivative: f'(x) = (pi/2) * cos(pi/2 * x)
    slope = (np.pi / 2) * np.cos(np.pi/2 * xm)
    
    half_seg = dx / 2
    xt = np.linspace(xm - half_seg, xm + half_seg, 50)
    yt = ym + slope * (xt - xm)
    plt.plot(
        xt, yt, 'b--', linewidth=1,
        label='Tangent approximation' if j == 0 else ""
    )

plt.xlim(a - 0.05, b + 0.05)
plt.ylim(0, 1.1)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'$\sin(\pi x / 2)$ with 4 step rectangles and tangent segments')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()