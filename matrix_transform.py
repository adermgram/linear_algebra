
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Initial matrix
initial = [2.0, 0.0, 0.0, 1.0]

fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.34)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect("equal")
ax.grid(True, alpha=0.25)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

# Original grid lines
grid_values = np.arange(-5, 6)

for i in grid_values:
    ax.plot(
        [-5, 5], [i, i],
        color="gray", alpha=0.15, linestyle="--"
    )
    ax.plot(
        [i, i], [-5, 5],
        color="gray", alpha=0.15, linestyle="--"
    )

# Create matrix controls
slider_axes = [
    plt.axes([0.20, 0.25, 0.65, 0.025]),
    plt.axes([0.20, 0.20, 0.65, 0.025]),
    plt.axes([0.20, 0.15, 0.65, 0.025]),
    plt.axes([0.20, 0.10, 0.65, 0.025])
]

s_a = Slider(slider_axes[0], "a", -3, 3, valinit=initial[0])
s_b = Slider(slider_axes[1], "b", -3, 3, valinit=initial[1])
s_c = Slider(slider_axes[2], "c", -3, 3, valinit=initial[2])
s_d = Slider(slider_axes[3], "d", -3, 3, valinit=initial[3])

def transform_point(x, y, A):
    point = np.array([x, y])
    return A @ point

def update(_=None):
    ax.clear()

    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.25)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)

    A = np.array([
        [s_a.val, s_b.val],
        [s_c.val, s_d.val]
    ])

    # Transform grid lines
    t = np.linspace(-5, 5, 100)

    for k in range(-5, 6):
        vertical = np.array([
            np.full_like(t, k),
            t
        ])

        horizontal = np.array([
            t,
            np.full_like(t, k)
        ])

        tv = A @ vertical
        th = A @ horizontal

        ax.plot(tv[0], tv[1], color="gray", alpha=0.35)
        ax.plot(th[0], th[1], color="gray", alpha=0.35)

    # Transform basis vectors
    ex = A @ np.array([1, 0])
    ey = A @ np.array([0, 1])

    ax.quiver(
        0, 0, ex[0], ex[1],
        angles="xy", scale_units="xy", scale=1,
        color="blue", width=0.012,
        label="First column: A(1,0)"
    )

    ax.quiver(
        0, 0, ey[0], ey[1],
        angles="xy", scale_units="xy", scale=1,
        color="red", width=0.012,
        label="Second column: A(0,1)"
    )

    ax.set_title(
        f"Matrix transformation\n"
        f"A = [[{A[0,0]:.2f}, {A[0,1]:.2f}], "
        f"[{A[1,0]:.2f}, {A[1,1]:.2f}]]"
    )

    ax.legend(loc="upper left")
    fig.canvas.draw_idle()

for slider in [s_a, s_b, s_c, s_d]:
    slider.on_changed(update)

reset_ax = plt.axes([0.40, 0.02, 0.20, 0.045])
reset_button = Button(reset_ax, "Reset")

def reset(_):
    s_a.reset()
    s_b.reset()
    s_c.reset()
    s_d.reset()

reset_button.on_clicked(reset)

update()
plt.show()