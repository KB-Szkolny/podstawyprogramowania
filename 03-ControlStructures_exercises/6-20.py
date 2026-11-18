# Pobiera od użytkownika liczbę dziesiętną w postaci tekstu (string) i zapisuje ją w zmiennej
input_number = input("Enter your decimal number: ")

# Konwertuje pobrany tekst na liczbę całkowitą (integer), aby móc wykonywać operacje matematyczne
decimal_number = int(input_number)

# Inicjalizuje pusty ciąg znaków, w którym będzie budowany wynikowy kod binarny (bity)
binary = ""

# Pętla wykonuje się tak długo, aż liczba dziesiętna będzie większa od zera
while decimal_number > 0:
  # Oblicza resztę z dzielenia liczby przez 2 (będzie to kolejna cyfra binarna: 0 lub 1)
  remainder = decimal_number % 2

  # Dzieli liczbę całkowicie przez 2 (zastępuje liczbę wynikiem dzielenia całkowitego)
  decimal_number //= 2

  # Zamienia resztę na tekst i dokleja ją z LEWEJ strony obecnego ciągu binarnego
  # (robimy tak, ponieważ reszty otrzymujemy od najmniej znaczącego bitu)
  binary = str(remainder) + binary

# Wyświetla sformatowany wynik końcowy: liczbę dziesiętną oraz jej odpowiednik w systemie binarnym
print(f"{input_number}(10) = {binary}(2)")