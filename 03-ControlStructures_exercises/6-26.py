# Definiuje poprawny kod PIN wymagany do autoryzacji płatności
pin_code = "0805"

# Inicjalizuje licznik nieudanych prób, ustawiając go na początkową wartość 0
amount_of_tries = 0

# Pętla pozwala użytkownikowi na podanie kodu PIN maksymalnie 3 razy (dla i = 0, 1, 2)
for i in range(0, 3):
  # Pobiera od użytkownika wpisany kod PIN
  attempts = input("Enter the PIN code: ")

  # Sprawdza, czy wpisany kod jest różny od poprawnego PIN-u
  if attempts != pin_code:
    print("Incorrect...")  # Informuje o błędnym kodzie
    amount_of_tries += 1  # Zwiększa licznik nieudanych prób o 1
  else:
    # Wykonuje się, gdy wpisany kod PIN jest poprawny
    print("Payment went through")
    break  # Przerywa pętlę, ponieważ płatność powiodła się i nie trzeba pytać dalej

# Po wyjściu z pętli sprawdza, czy liczba nieudanych prób osiągnęła 3
if amount_of_tries == 3:
  # Wyświetla komunikat o zablokowaniu karty po wyczerpaniu wszystkich prób
  print("Sorry, your payment card has been blocked")