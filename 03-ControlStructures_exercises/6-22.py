# Pętla iteruje przez liczby od 1 do 30 włącznie (funkcja range kończy się przed 31)
for i in range(1, 31):

  # Sprawdza, czy liczba jest podzielna jednocześnie przez 3 i przez 5 (reszta z dzielenia wynosi 0)
  if i % 3 == 0 and i % 5 == 0:
    i = "BINGO"  # Jeśli tak, zmienia wartość zmiennej 'i' na tekst "BINGO"

  # Jeśli nie była podzielna przez oba, sprawdza czy jest podzielna tylko przez 3
  elif i % 3 == 0:
    i = "THREE"  # Jeśli tak, zmienia wartość zmiennej 'i' na tekst "THREE"

  # Jeśli poprzednie warunki nie zostały spełnione, sprawdza czy jest podzielna tylko przez 5
  elif i % 5 == 0:
    i = "FIVE"  # Jeśli tak, zmienia wartość zmiennej 'i' na tekst "FIVE"

  # Wyświetla na ekranie aktualną wartość 'i'
  # (będzie to liczba w niezmienionej formie albo słowo "BINGO", "THREE" lub "FIVE")
  print(i)