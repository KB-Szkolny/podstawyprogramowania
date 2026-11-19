# Zadanie 3-4
arr = [-15, 8, -31, 47, -2, 19]

# Szukamy minimum i maksimum bez użycia funkcji min() oraz max()
minimum = arr[0]
maximum = arr[0]

for num in arr[1:]:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Minimum:", minimum)
print("Maximum:", maximum)