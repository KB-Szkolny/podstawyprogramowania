# Tworzy zmienną przechowującą znak gwiazdki ze spacją, która będzie budulcem wzoru
star = "* "

# Pierwsza pętla rysuje rosnącą część trójkąta (od 1 do 5 gwiazdek)
for i in range(1, 6):
  # Mnoży tekst przez liczbę 'i' (powtarza go) i wyświetla wynik
  print(star * i)

# Druga pętla rysuje malejącą część trójkąta (od 4 do 1 gwiazdek)
# Parametr -1 oznacza, że pętla odlicza w dół
for i in range(4, 0, -1):
  # Mnoży tekst przez malejącą wartość 'i' i wyświetla wynik
  print(star * i)