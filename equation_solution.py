import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)

# Equation 1:
# x + y = 5
y1 = 5 - x

# Equation 2:
# x - y = 1
y2 = x - 1

plt.figure(figsize=(8, 8))

plt.plot(x, y1, label="x + y = 5")
plt.plot(x, y2, label="x - y = 1")

# Solution
plt.scatter(3, 2, s=100)

plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.grid(True, alpha=0.3)
plt.xlabel("x")
plt.ylabel("y")

plt.title("System of Linear Equations")
plt.legend()

plt.show()