# Wyświetla nagłówek rozpoczynający ankietę na ekranie
print("--SURVEY--")

# Pobiera od użytkownika odpowiedź na pierwsze pytanie (czy interesuje się informatyką)
first_q = input("Are you intrested in computer science? (y/n): ")

# Pobiera odpowiedź na drugie pytanie (czy lubi grać w gry komputerowe)
second_q = input("Do you like playing computer games? (y/n): ")

# Pobiera odpowiedź na trzecie pytanie (czy posiada konto na Instagramie)
third_q = input("Do you have an Instagram account? (y/n): ")

# Sprawdza, czy wpisano 'y' lub 'Y' dla informatyki i ustawia zmienną logiczną na True lub False
if first_q == 'y' or first_q == 'Y':
  computer_science = True
else:
  computer_science = False

# Sprawdza, czy wpisano 'y' lub 'Y' dla gier i ustawia zmienną logiczną na True lub False
if second_q == 'y' or second_q == 'Y':
  computer_games = True
else:
  computer_games = False

# Sprawdza, czy wpisano 'y' lub 'Y' dla Instagrama i ustawia zmienną logiczną na True lub False
if third_q == 'y' or third_q == 'Y':
  ig_acc = True
else:
  ig_acc = False

# Zamienia wartość logiczną (True/False) na czytelny tekst 'Yes' lub 'No' dla informatyki
if computer_science:
  computer_science = "Yes"
else:
  computer_science = "No"

# Zamienia wartość logiczną na tekst 'Yes' lub 'No' dla gier komputerowych
if computer_games:
  computer_games = "Yes"
else:
  computer_games = "No"

# Zamienia wartość logiczną na tekst 'Yes' lub 'No' dla konta na Instagramie
if ig_acc:
  ig_acc = "Yes"
else:
  ig_acc = "No"

# Wyświetla nagłówek podsumowujący wyniki ankiety
print(f"--SURVEY RESULTS--")

# Wyświetla sformatowany wynik dotyczący zainteresowania informatyką
print(f"Intrested in computer science: {computer_science}")

# Wyświetla sformatowany wynik dotyczący grania w gry komputerowe
print(f"Playing computer games: {computer_games}")

# Wyświetla sformatowany wynik dotyczący posiadania konta na Instagramie
print(f"Has an Instagram account: {ig_acc}")