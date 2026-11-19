# Zadanie 3-30
mult_table = [[0 for _ in range(5)] for _ in range(5)]

# Wypełniamy tabliczkę mnożenia 5x5
for i in range(5):
    for j in range(5):
        mult_table[i][j] = (i + 1) * (j + 1)

for row in mult_table:
    print(*row)