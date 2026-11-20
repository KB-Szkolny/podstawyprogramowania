# Zadanie 3-5
arr = [15, 8, 31, 47, 2, 19]
total = 0

# Sumujemy elementy w pętli for[cite: 13]
for value in arr:
    total += value

mean = total / len(arr)
print("Array:", *arr)
print(f"Arithmetic mean: {mean:.2f}")