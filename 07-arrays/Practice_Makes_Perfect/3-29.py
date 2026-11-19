# Zadanie 3-29
def create_2d_arr(x, y):
    # Tworzy tablicę 2D o wymiarach x na y wypełnioną zerami
    return [[0 for _ in range(y)] for _ in range(x)]

arr_3x5 = create_2d_arr(3, 5)
for row in arr_3x5:
    print(*row)