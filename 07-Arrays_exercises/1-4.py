# Zadanie 1-4
arr = [2, 3, 7, 5, 4]

print(arr)  # 1. cała tablica
print('Number of elements', len(arr))  # 2. liczba elementów
print('First value', arr[0])  # 3. pierwszy element (indeks 0)
print('Second value', arr[1])  # 4. drugi element (indeks 1)
print('Last value', arr[len(arr) - 1])  # 5. ostatni element bez ujemnego indeksu
print('Last but one value', arr[len(arr) - 2])  # 6. przedostatni element bez ujemnego indeksu
print('Sum of first and last', arr[0] + arr[-1])  # 7. suma pierwszego i ostatniego elementu
print('Middle value', arr[len(arr) // 2])  # 8. środkowy element (dzielenie całkowite //)

# 9. wypisanie wszystkich elementów oddzielonych pojedynczą spacją w pętli
for x in arr:
    print(x, end=' ')
print()  # przejście do nowej linii po zakończeniu pętli