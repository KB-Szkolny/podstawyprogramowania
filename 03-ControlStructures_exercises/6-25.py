# Pętla iteruje przez zmienną 'i' od 1 do 9 włącznie (funkcja range kończy się przed 10)
for i in range(1, 10):
  # 1. str(i) zamienia aktualną liczbę (np. 3) na tekst ('3').
  # 2. * i powtarza ten tekst tyle razy, ile wynosi wartość 'i' (np. '3' * 3 daje '333').
  # 3. print(...) wyświetla wynik na ekranie.
  print(str(i) * i)