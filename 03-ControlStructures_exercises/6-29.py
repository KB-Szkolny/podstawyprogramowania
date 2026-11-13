# Wyświetla nagłówek programu informujący o jego przeznaczeniu
print("--Program that finds N leading prime numbers---")

# Pobiera od użytkownika liczbę N (ile pierwszych liczb pierwszych ma zostać znalezionych)
# i konwertuje ją z tekstu na liczbę całkowitą (integer)
n = int(input("Enter N: "))

# Inicjalizuje licznik znalezionych liczb pierwszych, ustawiając go na początkową wartość 0
count = 0

# Inicjalizuje zmienną 'candidate' (kandydat na liczbę pierwszą) wartością 2,
# ponieważ 2 jest pierwszą najmniejszą liczbą pierwszą.
candidate = 2

# Pętla główna wykonuje się tak długo, dopóki liczba znalezionych liczb pierwszych ('count')
# jest mniejsza niż żądana przez użytkownika ilość 'n'.
while count < n:
  # Zakłada na początku, że aktualnie sprawdzany kandydat jest liczbą pierwszą (flaga logiczna)
  is_prime = True

  # Pętla wewnętrzna sprawdza potencjalne dzielniki kandydata od 2 do wartości mniejszej od kandydata
  for divisor in range(2, candidate):
    # Sprawdza, czy kandydat dzieli się przez dany dzielnik bez reszty (reszta wynosi 0)
    if candidate % divisor == 0:
      is_prime = False  # Jeśli tak, to znaczy, że nie jest liczbą pierwszą – zmieniamy flagę na False
      break  # Przerywa wewnętrzną pętlę, bo znaleziono dzielnik (dalsze sprawdzanie nie ma sensu)

  # Po sprawdzeniu wszystkich dzielników, jeśli flaga nadal wynosi True, to liczba jest pierwsza
  if is_prime:
    print(candidate, end=" ")  # Wyświetla znalezioną liczbę pierwszą i kończy spacją
    count += 1  # Zwiększa licznik znalezionych liczb pierwszych o 1

  # Zwiększa wartość kandydata o 1 przed przejściem do kolejnej iteracji pętli
  candidate += 1