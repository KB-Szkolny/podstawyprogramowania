import math    # Importuje moduł 'math' zawierający funkcję sqrt() (pierwiastek kwadratowy)

a = 5     # Pierwszy bok prostokąta (int)
b = 8        # Drugi bok prostokąta (int)

diagonal = math.sqrt(a**2 + b**2)   # Oblicza przekątną ze wzoru Pitagorasa: sqrt(a^2 + b^2)

print("Diagonal = ", diagonal)    # Wypisuje wyliczoną długość przekątnej (daje float)