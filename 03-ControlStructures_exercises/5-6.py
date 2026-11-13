###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 11  # Przypisuje wartość 11 do zmiennej N, która określa górny zakres liczb
i = 1  # Przypisuje wartość 1 do zmiennej i, która służy jako licznik pętli
sum_even = 0  # Przypisuje wartość 0 do zmiennej sum_even, która będzie przechowywać sumę liczb parzystych
while i<= N:  # Rozpoczyna pętlę, która wykonuje się dopóki i jest mniejsze lub równe N
    if i%2 == 0:  # Sprawdza warunek: czy reszta z dzielenia i przez 2 jest równa 0, czyli czy liczba jest parzysta
        sum_even += i  # Jeśli warunek jest prawdziwy, dodaje aktualną wartość i do sumy liczb parzystych (sum_even)
    i += 1  # Zwiększa licznik (i) o 1, aby przejść do następnej liczby
# Calculate the sum of even numbers  # Obliczenie sumy liczb parzystych
# for i in range(1, N + 1):  # Alternatywna wersja z użyciem pętli for
#     if i % 2 == 0:  # Sprawdza czy liczba jest parzysta
#         sum_even += i  # Dodaje parzystą liczbę do sumy

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")  # Wypisuje sumę liczb parzystych od 1 do N