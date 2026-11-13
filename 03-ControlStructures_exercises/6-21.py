# Pobiera od użytkownika kwotę w PLN i konwertuje ją na liczbę całkowitą (integer)
amount = int(input("Enter the amount in PLN: "))

# Oblicza maksymalną liczbę monet 5 PLN mieszczących się w podanej kwocie (dzielenie całkowite)
five_pln = amount // 5

# Oblicza resztę pieniędzy pozostałą po wydaniu monet 5 PLN (operacja modulo)
rest_of_five = amount % 5

# Oblicza liczbę monet 2 PLN, które można wydać z reszty po pięciozłotówkach
two_pln = rest_of_five // 2

# Oblicza resztę po wydaniu również monet 2 PLN
rest_of_two = rest_of_five % 2

# To, co zostało z reszty, stanowi bezpośrednio liczbę potrzebnych monet 1 PLN
one_pln = rest_of_two

# Wyświetla nagłówek podsumowania oraz liczbę poszczególnych nominałów monet
print(f"The amount of {amount} PLN in coins: ")
print(f"5 PLN coins: {five_pln}")
print(f"2 PLN coins: {two_pln}")
print(f"1 PLN coins: {one_pln}")