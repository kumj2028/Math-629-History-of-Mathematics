import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

def draw_unit_circle_sector_vs_tan(x, n_circle=600):
    """
    Draw the full unit circle, shade the sector AOB (area = x/2 on unit circle),
    and shade the tangent triangle OAT (area = tan(x)/2) in a different color.

    Points:
      O = (0,0)
      A = (1,0)
      B = (cos x, sin x)
      T = (1, tan x) where ray OB meets tangent line x=1
    """
    if not (0 < x < np.pi/2):
        raise ValueError("x must be in (0, pi/2) radians.")

    O = np.array([0.0, 0.0])
    A = np.array([1.0, 0.0])
    B = np.array([np.cos(x), np.sin(x)])
    T = np.array([1.0, np.tan(x)])

    fig, ax = plt.subplots(figsize=(7.5, 7.5))

    # Full unit circle
    theta = np.linspace(0, 2*np.pi, n_circle)
    ax.plot(np.cos(theta), np.sin(theta), linewidth=2, label="Unit circle")

    # Shade sector AOB (0 to x), radius 1
    sector = Wedge(center=(0, 0), r=1.0, theta1=0, theta2=np.degrees(x), alpha=0.25, label="Sector AOB")
    ax.add_patch(sector)

    # Radii OA and OB (sector boundaries)
    ax.plot([O[0], A[0]], [O[1], A[1]], linewidth=2)
    ax.plot([O[0], B[0]], [O[1], B[1]], linewidth=2)

    # Tangent line at A: x = 1
    y_min = -1.2
    y_max = max(1.2, T[1] + 0.2)
    ax.plot([1, 1], [y_min, y_max], linestyle="--", linewidth=2, label="Tangent at A")

    # Ray from O through B extended to T
    ax.plot([O[0], T[0]], [O[1], T[1]], linewidth=2)

    # Shade tangent triangle OAT (different shading)
    tri_tan = np.vstack([O, A, T])
    ax.fill(tri_tan[:, 0], tri_tan[:, 1], alpha=0.25, label="Triangle OAT")

    # Points + labels
    ax.scatter([O[0], A[0], B[0], T[0]], [O[1], A[1], B[1], T[1]], s=60)
    ax.text(O[0]-0.06, O[1]-0.08, "O", fontsize=12)
    ax.text(A[0]+0.03, A[1]-0.06, "A", fontsize=12)
    ax.text(B[0]+0.03, B[1]+0.03, "B", fontsize=12)
    ax.text(T[0]+0.03, T[1]+0.03, "T", fontsize=12)

    # Annotate tan(x) as segment AT
    ax.annotate("tan(x)", xy=(1.0, T[1]/2), xytext=(1.1, T[1]/2),
                arrowprops=dict(arrowstyle="->"), fontsize=11)

    # Annotate arc length x (on unit circle)
    mid = x / 2
    ax.annotate("arc length = x", xy=(np.cos(mid), np.sin(mid)),
                xytext=(0.2, 0.35),
                arrowprops=dict(arrowstyle="->"), fontsize=11)

    # Formatting
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, max(1.35, T[1] + 0.3))
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_title(f"Sector (x) vs tangent triangle (tan x)")
    ax.legend(loc="upper left", fontsize=9)

    plt.show()


# Example:
draw_unit_circle_sector_vs_tan(np.pi/6)  # 30 degrees
