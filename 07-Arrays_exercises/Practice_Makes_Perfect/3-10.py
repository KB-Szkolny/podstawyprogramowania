# Zadanie 3-10
arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

# Wybieramy elementy z arr1, których nie ma w arr2
only_in_first = [x for x in arr1 if x not in arr2]

print("Numbers only in first array:", *only_in_first)