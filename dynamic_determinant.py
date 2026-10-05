import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# --------------------------------------------------
# Figure
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.30)


# --------------------------------------------------
# Sliders
# --------------------------------------------------

slider_a = Slider(
    plt.axes([0.20, 0.20, 0.60, 0.03]),
    "a",
    -3,
    3,
    valinit=1
)

slider_b = Slider(
    plt.axes([0.20, 0.15, 0.60, 0.03]),
    "b",
    -3,
    3,
    valinit=0
)

slider_c = Slider(
    plt.axes([0.20, 0.10, 0.60, 0.03]),
    "c",
    -3,
    3,
    valinit=0
)

slider_d = Slider(
    plt.axes([0.20, 0.05, 0.60, 0.03]),
    "d",
    -3,
    3,
    valinit=1
)


# --------------------------------------------------
# Draw function
# --------------------------------------------------

def draw():

    # Read matrix values
    A = np.array([
        [slider_a.val, slider_b.val],
        [slider_c.val, slider_d.val]
    ])

    # Determinant
    determinant = np.linalg.det(A)

    # Original unit square
    square = np.array([
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1],
        [0, 0]
    ])

    # Transform square
    transformed = (A @ square.T).T

    # Clear only the drawing area
    ax.clear()

    # --------------------------------------------------
    # Coordinate system
    # --------------------------------------------------

    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    ax.set_aspect("equal")
    ax.grid(True, alpha=0.25)

    # --------------------------------------------------
    # Draw original basis vectors
    # --------------------------------------------------

    ax.quiver(
        0, 0,
        1, 0,
        angles="xy",
        scale_units="xy",
        scale=1,
        width=0.008
    )

    ax.quiver(
        0, 0,
        0, 1,
        angles="xy",
        scale_units="xy",
        scale=1,
        width=0.008
    )

    # --------------------------------------------------
    # Draw transformed parallelogram
    # --------------------------------------------------

    ax.plot(
        transformed[:, 0],
        transformed[:, 1],
        linewidth=3
    )

    ax.fill(
        transformed[:, 0],
        transformed[:, 1],
        alpha=0.2
    )

    # --------------------------------------------------
    # Draw transformed basis vectors
    # --------------------------------------------------

    first_column = A[:, 0]
    second_column = A[:, 1]

    ax.quiver(
        0, 0,
        first_column[0],
        first_column[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        width=0.012
    )

    ax.quiver(
        0, 0,
        second_column[0],
        second_column[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        width=0.012
    )

    # --------------------------------------------------
    # Display information
    # --------------------------------------------------

    ax.set_title(
        "Matrix Transformation\n\n"
        f"A = [[{A[0,0]:.2f}, {A[0,1]:.2f}], "
        f"[{A[1,0]:.2f}, {A[1,1]:.2f}]]\n"
        f"det(A) = {determinant:.2f}"
    )

    fig.canvas.draw_idle()


# --------------------------------------------------
# Connect sliders
# --------------------------------------------------

slider_a.on_changed(lambda value: draw())
slider_b.on_changed(lambda value: draw())
slider_c.on_changed(lambda value: draw())
slider_d.on_changed(lambda value: draw())


# --------------------------------------------------
# Initial drawing
# --------------------------------------------------

draw()

plt.show()