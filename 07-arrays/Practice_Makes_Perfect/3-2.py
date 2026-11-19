# Zadanie 3-2
arr = [15, 8, 31, 47, 2, 19]
reversed_arr = []

# Przechodzimy od końca tablicy do początku
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

print("existed array:", *arr)
print("reverse array:", *reversed_arr)