# Zadanie 3-5
# Program pobiera od użytkownika nazwę i hasło do sprawdzenia.
username = input("Enter username: ")
password = input("Enter password: ")

# Nazwa użytkownika ma mieć co najmniej 6 małych liter.
username_pattern = r"[a-z]{6,}"
# Hasło ma mieć co najmniej 8 znaków: litery, cyfry lub podkreślenia.
password_pattern = r"[A-Za-z0-9_]{8,}"

# Dopasowanie obejmuje całą wartość, a nie tylko jej fragment.
username_match = re.fullmatch(username_pattern, username)
password_match = re.fullmatch(password_pattern, password)

# Dane są poprawne tylko wtedy, gdy zgadzają się nazwa i hasło.
if username_match and password_match:
    print("Username and password are valid.")
else:
    print("Username or password is invalid.")
