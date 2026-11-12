import math  # Importuje moduł 'math' potrzebny do obliczenia pierwiastka kwadratowego (math.sqrt)

h = float(input("Enter height in meters: "))  # Pobiera wysokość od użytkownika i konwertuje na liczbę z przecinkiem (float)
d = 3.57 * math.sqrt(h)     # Oblicza odległość do horyzontu ze wzoru: 3.57 * sqrt(h)

print("Distance to horizon:", round(d, 2), "km")  # Wypisuje wynik zaokrąglony do 2 miejsc po przecinku