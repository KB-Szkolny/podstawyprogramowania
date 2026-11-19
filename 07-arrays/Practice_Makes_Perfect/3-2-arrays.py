# Zadanie 3-2: tworzenie tablic
import random  # moduł do generowania liczb losowych[cite: 12]

arr1 = [3, 7, 1, 0, 4]
arr2 = [[2, 3], [7, 1], [0, 4]]
arr3 = [7 for _ in range(5)]
arr4 = [i for i in range(1, 10)]
arr5 = [i * 2 for i in range(1, 10)]
arr6 = [random.randint(1, 20) for _ in range(10)]
arr7 = [[] for _ in range(5)]
arr8 = [[1 for _ in range(4)] for _ in range(2)]
arr9 = [[random.randint(1, 20) for _ in range(5)] for _ in range(3)]

arr_custom = [4, 0, 3]
arr_zeros = [0] * 15
arr_range_1_30 = [random.randint(1, 30) for _ in range(10)]
arr_bits = [random.choice([0, 1]) for _ in range(20)]
arr_false_2d = [[False for _ in range(2)] for _ in range(5)]

for name, tab in [
    ("arr1", arr1), ("arr2", arr2), ("arr3", arr3), ("arr4", arr4), ("arr5", arr5),
    ("arr6", arr6), ("arr7", arr7), ("arr8", arr8), ("arr9", arr9),
    ("arr_custom", arr_custom), ("arr_zeros", arr_zeros), ("arr_range_1_30", arr_range_1_30),
    ("arr_bits", arr_bits), ("arr_false_2d", arr_false_2d)
]:
    print(f"{name}: {tab}")