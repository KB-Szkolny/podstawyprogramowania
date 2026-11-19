# Zadanie 3-12
arr = [2, 3, 2, 5, 8, 1, 9, 8]

# Zostawiamy tylko elementy występujące w tablicy dokładnie jeden raz
unique_elements = [x for x in arr if arr.count(x) == 1]

print("Array:", *arr)
print("Unique elements:", *unique_elements)