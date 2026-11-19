# Zadanie 3-36
def to_1d(arr_2d):
    return [item for row in arr_2d for item in row]

mat_i = [
    [2, 3],
    [1, 5]
]

mat_ii = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

mat_iii = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

print("i. 1D:", to_1d(mat_i))
print("ii. 1D:", to_1d(mat_ii))
print("iii. 1D:", to_1d(mat_iii))