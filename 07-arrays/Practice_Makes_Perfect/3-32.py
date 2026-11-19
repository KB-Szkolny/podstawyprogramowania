# Zadanie 3-32
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

# Zamieniamy pierwszy wiersz z ostatnim[cite: 18]
matrix[0], matrix[-1] = matrix[-1], matrix[0]

print("\nAfter swapping first and last row:")
print_matrix(matrix)