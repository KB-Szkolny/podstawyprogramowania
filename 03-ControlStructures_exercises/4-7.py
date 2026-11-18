###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0  # Przypisuje wartość 0 do zmiennej sum, która będzie przechowywać sumę liczb parzystych

for i in range(1,11):  # Rozpoczyna pętlę, która iteruje przez liczby od 1 do 10 (range(1,11) generuje wartości 1, 2, 3, ..., 10)
    if not i%2 == 0:  # Sprawdza warunek: czy reszta z dzielenia i przez 2 NIE jest równa 0, czyli czy liczba jest nieparzysta
        continue  # Jeśli warunek jest prawdziwy, pomija dalsze wykonanie bieżącej iteracji i przechodzi do następnej
    sum += i  # Jeśli liczba jest parzysta, dodaje aktualną wartość i do zmiennej sum

print(f'Sum of even numbers in the range <1,10> is {sum}')  # Wypisuje sumę liczb parzystych w zakresie <1,10>