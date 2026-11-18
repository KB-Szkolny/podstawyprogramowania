###
# Calculates x to the power of n using recursion
#
def power(x, n):
    if n == 0:       # Warunek bazowy: każda liczba podniesiona do potęgi 0 daje 1
        return 1
    else:        # Krok rekurencyjny: x^n = x * x^(n-1)
        return x * power(x, n - 1)

# Obliczenie 5^3 oraz 5^33
print('5^33 =', power(5, 33))