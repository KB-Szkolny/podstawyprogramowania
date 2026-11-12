password = input('Enter password: ')  # Pobiera hasło wprowadzone z klawiatury
password_ok = len(password) >= 8     # Sprawdza czy długość (len) wynosi co najmniej 8 znaków (True/False)
print(f'Password length is valid: {password_ok}')   # Wypisuje wynik sprawdzania (True lub False)