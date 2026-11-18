###
# Calculates the sum of natural numbers from 1 to n using recursion
#
def sum_natural(n):
    if n == 1:    # Warunek bazowy: suma dla n = 1 wynosi 1
        return 1
    else:            # Krok rekurencyjny: n + suma liczb od 1 do (n - 1)
        return n + sum_natural(n - 1)

# Obliczenie sumy liczb naturalnych w zakresie <1, 10>
result = sum_natural(10)
print(f'The sum of natural numbers from 1 to 10 is {result}')