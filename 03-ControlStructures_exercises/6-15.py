# Pobiera od użytkownika ciąg znaków (numer EAN-13) i zapisuje go w zmiennej ean_13
ean_13 = input("Enter EAN-13 article number: ")

# Sprawdza, czy wprowadzony ciąg znaków ma dokładnie 13 znaków
if len(ean_13) == 13:
  print("Article number is correct")

  # Sprawdza, czy pierwsze 3 cyfry to '590'.
  # W systemie kodów EAN prefiks '590' jest przypisany do Polski.
  if ean_13[0:3] == "590":
    print("Article manufactured in Poland")
  else:
    print("Article not manufactured in Poland")

# Wykonuje się, jeśli długość wprowadzonego tekstu nie wynosi dokładnie 13 znaków
else:
  print("Incorrect article number!")