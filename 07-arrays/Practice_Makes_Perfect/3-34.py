# Zadanie 3-34
def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def print_2d(matrix):
    for row in matrix:
        print(*row)
    print()

for size in [3, 5, 8]:
    print(f"Identity matrix {size}x{size}:")
    print_2d(identity_matrix(size))