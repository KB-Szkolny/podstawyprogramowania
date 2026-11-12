# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.

swift = input('Enter SWIFT code: ')      # Pobiera kod SWIFT od użytkownika

print(f'Bank Code: {swift[0:4]}')        # Wypisuje pierwsze 4 znaki (kod banku)
print(f'Country Code: {swift[4:6]}')     # Wypisuje 5. i 6. znak (kod kraju)