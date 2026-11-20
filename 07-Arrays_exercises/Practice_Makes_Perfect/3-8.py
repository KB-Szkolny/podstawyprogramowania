# Zadanie 3-8
arr = [2, 6, 4, 9, 7]

def star(n):
    # Zwracamy napis złożony z n gwiazdek[cite: 13]
    return "*" * n

for number in arr:
    print(f"{number}: {star(number)}")