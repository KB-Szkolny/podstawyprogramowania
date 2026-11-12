import math  # Importuje moduł math, aby użyć wartości liczby Pi

# Pobiera obwód drzewa i zamienia go na liczbę 
tree_circumference = float(input('Enter tree circumference in cm: '))

# Oblicza średnicę drzewa ze wzoru: średnica = obwód / Pi
tree_diameter = tree_circumference / math.pi

# Sprawdza czy średnica wynosi co najmniej 50 cm 
can_be_cut = tree_diameter >= 50

print(f'Tree can be cut down: {can_be_cut}')