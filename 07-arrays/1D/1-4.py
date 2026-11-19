# Zadanie 1-4
arr = [2, 3, 7, 5, 4]

print(arr)  # i. cała tablica
print('Number of elements', len(arr))  # ii. liczba elementów[cite: 1]
print('First value', arr[0])  # iii. pierwszy element (indeks 0)[cite: 1]
print('Second value', arr[1])  # iv. drugi element (indeks 1)[cite: 1]
print('Last value', arr[len(arr) - 1])  # v. ostatni element bez ujemnego indeksu[cite: 1]
print('Last but one value', arr[len(arr) - 2])  # vi. przedostatni element bez ujemnego indeksu[cite: 1]
print('Sum of first and last', arr[0] + arr[-1])  # vii. suma pierwszego i ostatniego elementu[cite: 1]
print('Middle value', arr[len(arr) // 2])  # viii. środkowy element (dzielenie całkowite //)[cite: 1]

# ix. wypisanie wszystkich elementów oddzielonych pojedynczą spacją w pętli[cite: 1]
for x in arr:
    print(x, end=' ')
print()  # przejście do nowej linii po zakończeniu pętli