import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [2, 1],
    [1, 2]
])

# Unit square
square = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [0, 0]
])

# Transform every point
transformed = (A @ square.T).T

det = np.linalg.det(A)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Original
axes[0].plot(square[:, 0], square[:, 1], linewidth=3)
axes[0].fill(square[:, 0], square[:, 1], alpha=0.2)

axes[0].set_title("Original unit square")

# Transformed
axes[1].plot(
    transformed[:, 0],
    transformed[:, 1],
    linewidth=3
)

axes[1].fill(
    transformed[:, 0],
    transformed[:, 1],
    alpha=0.2
)

axes[1].set_title(
    f"Transformed shape\n"
    f"det(A) = {det:.2f}"
)

for ax in axes:
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.grid(True, alpha=0.3)
    ax.set_aspect("equal")

plt.tight_layout()
plt.show()