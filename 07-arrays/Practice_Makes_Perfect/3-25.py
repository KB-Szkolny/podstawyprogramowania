# Zadanie 3-25
import matplotlib.pyplot as plt

x = []
y = []

# Generujemy wartości x w zakresie od -100 do 100
for n in range(-100, 101):
    x.append(n)

# Obliczamy wartości funkcji f(x) = x^2 - 3
for n in x:
    y.append(n ** 2 - 3)

plt.plot(x, y)
plt.title("Graph of f(x) = x^2 - 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()