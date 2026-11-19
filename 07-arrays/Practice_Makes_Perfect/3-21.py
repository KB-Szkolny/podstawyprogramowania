# Zadanie 3-21
arr1 = [2, 5, 8]
arr2 = [8, 1, 2, 9, 5, 3]

# Sprawdzamy, czy wszystkie elementy arr1 znajdują się w arr2
is_subset = all(elem in arr2 for elem in arr1)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Is array 1 a subset of array 2?", is_subset)