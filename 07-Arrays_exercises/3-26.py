# Zadanie 3-26
import math
import matplotlib.pyplot as plt

angles_deg = list(range(0, 361))
sin_values = [math.sin(math.radians(deg)) for deg in angles_deg]

plt.plot(angles_deg, sin_values)
plt.title("Graph of y = sin(x)")
plt.xlabel("Angle (degrees)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()