###
# Credit card payment
#
account_balance = 500  # Przypisuje wartość 500 do zmiennej account_balance, która przechowuje saldo konta
total_payment = float(input('Wpisz kwote transakcji: '))  # Wypisuje komunikat proszący użytkownika o wpisanie kwoty, pobiera wpisany tekst, konwertuje go na liczbę zmiennoprzecinkową i przypisuje do zmiennej total_payment

if total_payment < account_balance:  # Sprawdza warunek: czy kwota transakcji (total_payment) jest mniejsza niż saldo konta (account_balance)
    print('Payment completed')  # Jeśli warunek jest prawdziwy, wypisuje komunikat o pomyślnym zakończeniu płatności
else:  # Jeśli warunek (total_payment < account_balance) jest fałszywy, czyli kwota transakcji jest większa lub równa saldu
    print('No funds')  # Wypisuje komunikat o braku środków na koncie