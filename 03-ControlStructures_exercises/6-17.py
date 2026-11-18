# Pobiera od użytkownika czas w formacie 24-godzinnym (np. "14:30") i zapisuje go w zmiennej
time_24 = input("Enter time in 24hr format (hh:mm): ")

# Dzieli wprowadzony tekst na dwie części (godzinę i minuty) w miejscu wystąpienia dwukropka
parts = time_24.split(":")

# Pobiera pierwszą część (godzinę) i konwertuje ją z tekstu (string) na liczbę całkowitą (int)
hour = int(parts[0])

# Przypisuje drugą część (minuty) do zmiennej 'minutes' jako tekst
minutes = parts[1]

# Wyświetla pierwotnie wprowadzony czas w formacie 24-godzinnym
print(f"Time in 24-hour format: {time_24}")

# Sprawdza, czy godzina to północ (0:00)
if hour == 0:
  print(f"Time in 12-hour format: 12:{minutes}am")

# Sprawdza, czy godzina mieści się w przedziale od 1 do 11 (godziny poranne/przedpołudniowe)
if hour > 0 and hour <= 11:
  print(f"Time in 12-hour format: {hour}:{minutes}am")

# Sprawdza, czy jest dokładnie w południe (12:00)
if hour == 12:
  print(f"Time in 12-hour format: 12:{minutes}pm")

# Sprawdza, czy godzina jest z przedziału popołudniowego/wieczornego (od 13 do 23)
if hour > 12 and hour <= 23:
  # Odejmuje 12 od godziny, aby przekształcić ją na format 12-godzinny i dodaje 'pm'
  print(f"Time in 12-hour format: {hour - 12}:{minutes}pm")