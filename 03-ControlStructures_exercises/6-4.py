###
# Password validator
# New password is at least 12 characters long
#
new_password = input('Enter new password: ')  # Wypisuje komunikat proszący użytkownika o wpisanie nowego hasła i przypisuje wpisany tekst do zmiennej new_password
repeat_password = input('Repeat your password: ')  # Wypisuje komunikat proszący użytkownika o powtórzenie hasła i przypisuje wpisany tekst do zmiennej repeat_password

if new_password == repeat_password:  # Sprawdza warunek: czy nowe hasło (new_password) jest równe powtórzonemu hasłu (repeat_password)
    if len(new_password) < 12:  # Jeśli hasła się zgadzają, sprawdza czy długość nowego hasła jest mniejsza niż 12 znaków
        print('Password too short (min. 12 chars)')  # Jeśli warunek jest prawdziwy, wypisuje komunikat o zbyt krótkim haśle
    else:  # Jeśli długość hasła jest większa lub równa 12 znakom
        print('Password confirmed')  # Wypisuje komunikat o potwierdzeniu hasła
else:  # Jeśli hasła się nie zgadzają
    print("The passwords doesnt match! Check the spelling")  # Wypisuje komunikat o niepasujących hasłach i prosi o sprawdzenie pisowni