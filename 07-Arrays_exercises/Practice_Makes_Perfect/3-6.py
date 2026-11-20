# Zadanie 3-6
arr = [15, 8, 31, 47, 2, 19]
total = 0
i = 0

# Sumujemy elementy w pętli while[cite: 13]
while i < len(arr):
    total += arr[i]
    i += 1

mean = total / len(arr)
print("Array:", *arr)
print(f"Arithmetic mean: {mean:.2f}")