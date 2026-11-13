###
# Calculates the sum of integer numbers in the range <1,5>
#
sum = 0  # Przypisuje wartość 0 do zmiennej sum, która będzie przechowywać sumę liczb

for i in range(5,11):  # Rozpoczyna pętlę, która iteruje przez liczby od 5 do 10 (range(5,11) generuje wartości 5, 6, 7, 8, 9, 10)
    sum += i  # Dodaje aktualną wartość i do zmiennej sum

print(f'Sum is {sum}')  # Wypisuje obliczoną sumę