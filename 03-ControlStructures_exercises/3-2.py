###
# Checking login and password
#
login = 'joe'  # Przypisuje wartość 'joe' do zmiennej login, która przechowuje poprawny login
password = 'abcd'  # Przypisuje wartość 'abcd' do zmiennej password, która przechowuje poprawne hasło
entered_login = input('Login: ')  # Wypisuje komunikat proszący użytkownika o wpisanie loginu i przypisuje wpisany tekst do zmiennej entered_login
entered_password = input('Password: ')  # Wypisuje komunikat proszący użytkownika o wpisanie hasła i przypisuje wpisany tekst do zmiennej entered_password
if login == entered_login and password == entered_password :  # Sprawdza warunek: czy wpisany login (entered_login) jest równy poprawnemu loginowi (login) ORAZ czy wpisane hasło (entered_password) jest równe poprawnemu hasłu (password)
    print('You are logged in')  # Jeśli warunek jest prawdziwy, wypisuje komunikat o pomyślnym zalogowaniu
else:  # Jeśli warunek jest fałszywy, czyli login lub hasło są niepoprawne
    print('Incorrect login or password!!')  # Wypisuje komunikat o niepoprawnym loginie lub haśle