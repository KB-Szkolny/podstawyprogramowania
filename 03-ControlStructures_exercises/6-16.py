# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#

# Pobiera od użytkownika wybór programu prania: (j)acket, (u)nderwear, (s)hoes
washing_product = input(
    "Select washing program: (j)acket, (u)nderwear, (s)hoes "
)

# Pobiera informację od użytkownika, czy chce dodatkowe płukanie (y/n)
rinse = input("Extra rinse? (y/n) ")

# Pobiera informację od użytkownika, czy chce dodatkowe wirowanie (y/n)
spin = input("Extra spin? (y/n) ")

# Inicjalizuje zmienną przechowującą całkowity czas prania wartością 0
washing_time = 0

# Sprawdza wybrany program prania (używając ciągłego łańcucha if-elif-else)
if washing_product == "j" or washing_product == "J":
  washing_time += 40  # Dodaje 40 minut dla kurtki
  washing_product = "Jacket"  # Zmienia skrót na pełną nazwę
elif washing_product == "u" or washing_product == "U":
  washing_time += 70  # Dodaje 70 minut dla bielizny
  washing_product = "Underwear"  # Zmienia skrót na pełną nazwę
elif washing_product == "s" or washing_product == "S":
  washing_time += 20  # Dodaje 20 minut dla butów
  washing_product = "Shoes"  # Zmienia skrót na pełną nazwę
else:
  print("Wrong character typed!")  # Wyświetla błąd, jeśli wpisano coś innego

# Sprawdza opcję dodatkowego płukania
if rinse == "y" or rinse == "Y":
  rinse = True
  spin = False
  washing_time += 15  # Dodaje 15 minut za dodatkowe płukanie
elif rinse == "n" or rinse == "N":
  rinse = False
  # Jeśli nie wybrano płukania, sprawdza opcję dodatkowego wirowania
  if spin == "y" or spin == "Y":
    spin = True
    washing_time += 9  # Dodaje 9 minut za dodatkowe wirowanie
  elif spin == "n" or spin == "N":
    spin = False
  else:
    print(
        "Wrong character typed!"
    )  # Błąd, jeśli wpisano niepoprawny znak przy wirowaniu
else:
  print(
      "Wrong character typed!"
  )  # Błąd, jeśli wpisano niepoprawny znak przy płukaniu

# Wyświetla końcowe podsumowanie parametrów prania oraz całkowity czas
print(f"Washing product: {washing_product}")
print(f"Rinse: {rinse}")
print(f"Spin: {spin}")
print(f"Total washing time: {washing_time}")