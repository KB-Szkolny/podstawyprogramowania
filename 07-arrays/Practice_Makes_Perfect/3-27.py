# Zadanie 3-27
arr_2d = [
    [10, 20, 30, 40],
    [50, 60, 70, 80]
]

# Wypisujemy wartości w wierszach i kolumnach[cite: 17]
for row in arr_2d:
    for val in row:
        print(val, end=" ")
    print()