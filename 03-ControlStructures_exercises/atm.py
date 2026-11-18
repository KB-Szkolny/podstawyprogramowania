# --- ATM (cash machine) simulator ---

# Inicjalizacja stanu początkowego bankomatu
balance = 1000  # Początkowe saldo konta (1000 euro)
pin = "1111"  # Początkowy, 4-cyfrowy kod PIN

# Główna pętla programu, która działa bez końca, dopóki użytkownik nie wybierze opcji wyjścia
while True:
  print()  # Wyświetla pustą linię dla czytelności interfejsu
  print("ATM Menu:")
  print("1. Check balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Check PIN")
  print("5. Change PIN")
  print("6. Exit")

  # Pobiera od użytkownika wybór opcji z menu (jako tekst)
  choice = input("Choose an option (1-4): ")  # (Uwaga w tekście: zakres 1-6)
  print()

  # Opcja 1: Sprawdzenie aktualnego salda konta
  if choice == "1":
    print(f"Your current balance is: €{balance}")

  # Opcja 2: Wpłata środków na konto
  elif choice == "2":
    amount = float(input("Enter the amount to deposit: "))  # Pobiera kwotę wpłaty
    balance += amount  # Zwiększa saldo o wpłaconą kwotę
    print(f"€{amount} has been deposited. New balance: €{balance}")

  # Opcja 3: Wypłata środków z konta
  elif choice == "3":
    amount = float(input("Enter the amount to withdraw: "))  # Pobiera kwotę wypłaty
    # Sprawdza, czy żądana kwota nie przekracza dostępnego salda
    if amount <= balance:
      balance -= amount  # Zmniejsza saldo o wypłaconą kwotę
      print(f"€{amount} has been withdrawn. New balance: €{balance}")
    else:
      print("Insufficient balance.")  # Komunikat o braku wystarczających środków

  # Opcja 4: Wyświetlenie aktualnego kodu PIN
  elif choice == "4":
    print(f"Your current PIN code is: {pin}")

  # Opcja 5: Zmiana kodu PIN
  elif choice == "5":
    new_pin = input("Enter your new PIN code: ")  # Pobiera nowy PIN
    # Sprawdza, czy wpisany nowy PIN składa się wyłącznie z cyfr
    if new_pin.isdigit() == True:
      # Sprawdza, czy nowy PIN jest inny niż dotychczasowy
      if new_pin != pin:
        pin_repeat = input("Repeat your new PIN code: ")  # Prosi o powtórzenie PIN-u
        # Sprawdza, czy oba wpisane nowe kody są identyczne
        if new_pin == pin_repeat:
          pin = new_pin  # Aktualizuje PIN na nowy
          print("Your PIN code has been changed.")
        else:
          print("PIN codes dont match!")  # Kody się nie zgadzają
      else:
        print("Your new PIN code is the same as the old one!")  # Nowy PIN jest taki sam jak stary
    else:
      print("Your new PIN code contains letters.")  # PIN zawiera litery zamiast cyfr

  # Opcja 6: Wyjście z programu
  elif choice == "6":
    print("Exiting... Thank you for using the ATM!")
    break  # Przerywa działanie pętli while i kończy program

  # Obsługa błędnego wyboru opcji z menu
  else:
    print("Invalid option. Please try again.")