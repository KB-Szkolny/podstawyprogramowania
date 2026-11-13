# Zewnętrzna pętla iteruje przez zmienną 'i' od 1 do 7 włącznie (reprezentuje początkowe wartości dla każdego wiersza)
for i in range(1, 8):

  # Wewnętrzna pętla iteruje przez zmienną 'j' od 0 do 6 włącznie (odpowiada za 7 kolejnych kolumn w wierszu)
  for j in range(0, 7):
    # Oblicza wartość liczbową według wzoru i + j * 7 (skoki co 7) i wyświetla ją, kończąc spacją zamiast nowej linii
    print(f"{i+j*7}", end=" ")

  # Po wypisaniu całego wiersza (7 liczb) wewnętrzna pętla się kończy,
  # a ta instrukcja wykonuje przejście do nowej linii (enter)
  print()