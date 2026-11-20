# Zadanie 2-6
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Główna przekątna macierzy kwadratowej ma równe indeksy wiersza i kolumny
for i in range(len(matrix)):
    matrix[i][i] = 1

for row in matrix:
    print(*row)