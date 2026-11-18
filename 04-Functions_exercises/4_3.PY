###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2       # Oblicza połowę obwodu trójkąta (semiperimeter)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))      # Oblicza pole ze wzoru Herona
    return area                # Zwraca obliczone pole

# Część 1: Odczytanie boków z klawiatury
side_a = float(input('Enter side a: '))       # Pobiera długość boku a
side_b = float(input('Enter side b: '))       # Pobiera długość boku b
side_c = float(input('Enter side c: '))    # Pobiera długość boku c

print(f'The area of a triangle with sides {side_a}, {side_b}, {side_c} is {triangle_area(side_a, side_b, side_c)}')

# Część 2: Obliczenia dla podanych wymiarów testowych
print(f'The area of a triangle with sides 3, 4, 5 is {triangle_area(3, 4, 5)}')
print(f'The area of a triangle with sides 5, 12, 13 is {triangle_area(5, 12, 13)}')
print(f'The area of a triangle with sides 7, 24, 25 is {triangle_area(7, 24, 25)}')