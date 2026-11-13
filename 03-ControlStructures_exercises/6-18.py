# Pobiera od użytkownika współrzędne punktu w formacie "x,y" (np. "3,-5") i zapisuje je w zmiennej
point = input("Enter coordinates of your point [P(x,y)]: ")

# Dzieli wprowadzony tekst na listę mniejszych części (elementów) w miejscu wystąpienia przecinka
coordinates = point.split(",")

# Pobiera pierwszą część (indeks 0), czyli współrzędną x, i konwertuje ją z tekstu na liczbę całkowitą
x = int(coordinates[0])

# Pobiera drugą część (indeks 1), czyli współrzędną y, i konwertuje ją z tekstu na liczbę całkowitą
y = int(coordinates[1])

# Wyświetla osobno wyciągnięte współrzędne x oraz y
print(f"x = {x}")
print(f"y = {y}")

# Sprawdza, czy x i y są dodatnie (I ćwiartka: x > 0, y > 0)
if x > 0 and y > 0:
  print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")

# Sprawdza, czy x jest ujemne, a y dodatnie (II ćwiartka: x < 0, y > 0)
elif x < 0 and y > 0:
  print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")

# Sprawdza, czy x i y są ujemne (III ćwiartka: x < 0, y < 0)
elif x < 0 and y < 0:
  print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")

# Sprawdza, czy x jest dodatnie, a y ujemne (IV ćwiartka: x > 0, y < 0)
elif x > 0 and y < 0:
  print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")

# Sprawdza, czy obie współrzędne wynoszą 0 (początek układu współrzędnych: punkt (0,0))
elif x == 0 and y == 0:
  print(f"Point P({x},{y}) is located at the origin of the coordinate system")

# Sprawdza, czy współrzędna x wynosi 0 (punkt leży dokładnie na osi Y)
elif x == 0:
  print(f"Point P({x},{y}) is located on Y axis")

# Sprawdza, czy współrzędna y wynosi 0 (punkt leży dokładnie na osi X)
elif y == 0:
  print(f"Point P({x},{y}) is located on X axis")