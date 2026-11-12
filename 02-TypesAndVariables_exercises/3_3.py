x = 7
y = 34
z = 0  # Zmienna pomocnicza (dodatkowa)
print("Before swapping: x=", x, "y=", y)

# Prawidłowa zamiana wartości za pomocą zmiennej pomocniczej z:
z = x  # 1. Przelewasz zawartość x do pustej zmiennej z (teraz z = 7)
x = y  # 2. Przelewasz zawartość y do x (teraz x = 34)
y = z  # 3. Przelewasz zawartość z do y (teraz y = 7)

print("After swapping: x=", x, "y=", y)