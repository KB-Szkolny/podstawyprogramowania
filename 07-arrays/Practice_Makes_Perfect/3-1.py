# Zadanie 3-1
arr = [34, 7, 19, 4, 21, 8]
even_count = 0
i = 0

# Zliczamy liczby parzyste za pomocą pętli while[cite: 12]
while i < len(arr):
    if arr[i] % 2 == 0:
        even_count += 1
    i += 1

print("Number of even values:", even_count)