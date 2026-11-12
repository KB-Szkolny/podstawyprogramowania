a = int(input('a='))  # Pobiera długość pierwszego boku prostopadłościanu jako liczbę całkowitą (int)
b = int(input('b='))  # Pobiera długość drugiego boku jako liczbę całkowitą (int)
c = int(input('c='))  # Pobiera długość trzeciego boku jako liczbę całkowitą (int)

volume = a * b * c      # Oblicza objętość prostopadłościanu ze wzoru V = a * b * c
surface_area = 2 * (a * b + a * c + b * c) # Oblicza pole powierzchni całkowitej ze wzoru Pc = 2(ab + ac + bc)

# Wypisuje objętość prostopadłościanu z podanymi bokami
print(f'The volume of a cuboid with sides {a}, {b}, {c} is {volume}')

# Wypisuje pole powierzchni całkowitej prostopadłościanu
print(f'The surface area of a cuboid with sides {a}, {b}, {c} is {surface_area}')