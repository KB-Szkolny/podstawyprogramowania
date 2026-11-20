# Zadanie 3-11
def bubblesort(array):
    arr = array[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arrays_to_sort = [
    [64, 34, 25, 12, 22, 11, 90],
    [-5, 10, 0, -20, 15],
    [3, 1, 2]
]

for idx, sample in enumerate(arrays_to_sort, start=1):
    print(f"Array {idx} sorted:", bubblesort(sample))