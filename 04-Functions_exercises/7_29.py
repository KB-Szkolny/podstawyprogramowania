###
# Calculates factorial of n using recursion
#
def factorial(n):        # Definicja funkcji liczącej silnię liczby n
    # 0! = 1, 1! = 1
    if n == 0 or n == 1:   # Warunek bazowy (stopu): dla 0 lub 1 wynik to 1
        return 1          # Zwrócenie wartości 1 i zakończenie rekurencji

    # n! = n * (n-1)!
    if n > 1:               # Krok rekurencyjny dla liczb większych od 1
        return n * factorial(n - 1)     # Mnożenie n przez wynik funkcji dla (n - 1)

# Obliczenie silni dla n = 5
result = factorial(5)         # Wywołanie funkcji dla argumentu 5 i zapis wyniku
print(f'5! = {result}')     # Wyświetlenie obliczonego wyniku na ekranie