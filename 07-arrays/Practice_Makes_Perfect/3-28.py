# Zadanie 3-28
grid = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# Sumujemy wartości z ostatniej kolumny (indeks -1)
last_col_sum = sum(row[-1] for row in grid)

print("Sum of values in the last column:", last_col_sum)