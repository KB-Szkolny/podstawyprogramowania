# A program that converts a decimal integer to binary and hexadecimal

number = int(input('Enter number: '))  # Pobiera liczbę dziesiętną od użytkownika (int)

binary_number = bin(number)    # Konwertuje liczbę na system binarny (dwójkowy)
hex_number = hex(number)    # Konwertuje liczbę na system szesnastkowy (heksadecymalny)

print(f'Binary number: {binary_number}')     # Wypisuje wynik w postaci binarnej 
print(f'Hexadecimal number: {hex_number}')   # Wypisuje wynik w postaci szesnastkowej 