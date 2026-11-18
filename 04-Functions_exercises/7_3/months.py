def month(n):                           # Definicja funkcji zwracającej nazwę miesiąca dla numeru 1-12
    months = [                          # Lista z nazwami wszystkich 12 miesięcy po angielsku
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    if 1 <= n <= 12:                    # Sprawdzenie, czy podany numer mieści się w zakresie od 1 do 12
        return months[n - 1]            # Zwrócenie odpowiedniego miesiąca (odejmujemy 1, bo lista indeksuje od 0)
    return "Invalid month number"       # Komunikat w razie podania liczby spoza zakresu

if __name__ == "__main__":              # Kod testowy przy bezpośrednim uruchomieniu pliku months.py
    print(month(7))                     # Wynik testu: July