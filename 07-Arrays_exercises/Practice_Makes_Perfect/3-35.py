# Zadanie 3-35
def transpose_matrix(m):
    return [list(col) for col in zip(*m)]

def print_2d(matrix):
    for row in matrix:
        print(*row)
    print()

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

m3 = [
    [5, 6, 7, 8]
]

for idx, mat in enumerate([m1, m2, m3], start=1):
    print(f"Transposed matrix {idx}:")
    print_2d(transpose_matrix(mat))