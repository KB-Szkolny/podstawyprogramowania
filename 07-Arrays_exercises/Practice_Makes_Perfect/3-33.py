# Zadanie 3-33
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

def print_matrix(m):
    for row in m:
        print(*row)

print("Before:")
print_matrix(matrix)

# Zamieniamy pierwszy i ostatni element w każdym wierszu[cite: 18]
for row in matrix:
    row[0], row[-1] = row[-1], row[0]

print("\nAfter swapping first and last column:")
print_matrix(matrix)