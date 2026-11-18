# Importuje moduł 'time', który umożliwia kontrolowanie czasu i opóźnianie działania programu
import time

# Pobiera od użytkownika liczbę sekund do odliczania i konwertuje ją na liczbę całkowitą (integer)
countdown = int(input("Enter the number of seconds to count down: "))

# Główna pętla wykonuje się tak długo, dopóki licznik sekund jest większy od zera
while countdown > 0:
  # Sprawdza, czy zostało dokładnie 5 sekund do końca
  if countdown == 5:
    print("five")  # Wyświetla słownie "five" zamiast liczby 5

  # Sprawdza, czy zostały 4 sekundy
  elif countdown == 4:
    print("four")  # Wyświetla słownie "four"

  # Sprawdza, czy zostały 3 sekundy
  elif countdown == 3:
    print("three")  # Wyświetla słownie "three"

  # Sprawdza, czy zostały 2 sekundy
  elif countdown == 2:
    print("two")  # Wyświetla słownie "two"

  # Sprawdza, czy została 1 sekunda
  elif countdown == 1:
    print("one")  # Wyświetla słownie "one"

  # Wykonuje się dla wszystkich pozostałych wartości licznika (większych niż 5)
  else:
    print(countdown)  # Wyświetla standardową cyfrę/liczbę

  # Zmniejsza wartość licznika sekund o 1 w każdej iteracji
  countdown -= 1

  # Wstrzymuje działanie programu na dokładnie 1 sekundę, symulując rzeczywisty upływ czasu
  time.sleep(1)

# Wyświetla komunikat końcowy po zakończeniu pętli (gdy odliczanie dobiegnie końca)
print("Time's up!")