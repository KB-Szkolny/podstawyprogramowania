import math  # Importuje moduł math, który zawiera dokładną wartość liczby Pi

# determine radius value
r = float(input('Enter radius (r): '))  # Pobiera promień i zamienia na liczbę zmiennoprzecinkową

# calculate area
area = math.pi * (r ** 2)       # Oblicza pole powierzchni ze wzoru

# calculate circumference
circumference = 2 * math.pi * r     # Oblicza obwód ze wzoru

# print results
print(f'Radius: {r}')                         # Wypisuje promień
print(f'Circumference: {circumference:.2f}')    # Wypisuje obwód zaokrąglony do 2 miejsc po przecinku
print(f'Area: {area:.2f}')                    # Wypisuje pole zaokrąglone do 2 miejsc po przecinku