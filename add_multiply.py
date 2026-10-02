
import numpy as np
import matplotlib.pyplot as plt

# Define two vectors
a = np.array([3, 2])
b = np.array([2, 4])

# Operations
result = a + b
scaled = 2 * a

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

def draw_vector(ax, vector, label, color, start=(0, 0)):
    ax.quiver(
        *start,
        vector[0],
        vector[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=color,
        width=0.012,
        label=label
    )

# First plot: individual vectors
draw_vector(axes[0], a, "a = (3, 2)", "blue")
draw_vector(axes[0], b, "b = (2, 4)", "red")

axes[0].set_title("Individual vectors")
axes[0].legend()

# Second plot: vector addition
draw_vector(axes[1], a, "a", "blue")
draw_vector(axes[1], b, "b", "red", start=a)
draw_vector(axes[1], result, "a + b", "green")

axes[1].set_title("Vector addition")
axes[1].legend()

# Third plot: scalar multiplication
draw_vector(axes[2], a, "a", "blue")
draw_vector(axes[2], scaled, "2a", "purple")

axes[2].set_title("Scalar multiplication")
axes[2].legend()

for ax in axes:
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 8)
    ax.set_aspect("equal")
    ax.grid(True)

plt.tight_layout()
plt.show()