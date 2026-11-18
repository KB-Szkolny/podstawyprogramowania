amount = int(input("Enter number of purchased products: "))  # Wypisuje komunikat proszący użytkownika o wpisanie liczby zakupionych produktów, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej amount
base_price = float(input("Enter product pirce: "))  # Wypisuje komunikat proszący użytkownika o wpisanie ceny produktu, pobiera wpisany tekst, konwertuje go na liczbę zmiennoprzecinkową i przypisuje do zmiennej base_price
if amount <= 2:  # Sprawdza warunek: czy liczba zakupionych produktów (amount) jest mniejsza lub równa 2
    amount_to_pay = base_price*amount  # Jeśli warunek jest prawdziwy, oblicza kwotę do zapłaty, mnożąc cenę produktu przez liczbę produktów (bez rabatu)
elif amount > 2:  # Jeśli poprzedni warunek jest fałszywy, czyli liczba zakupionych produktów jest większa niż 2
    discount = (base_price*amount) * 0.25  # Oblicza rabat, mnożąc całkowitą cenę (base_price * amount) przez 0.25 (25% rabatu)
    amount_to_pay = (base_price * amount) - discount  # Oblicza kwotę do zapłaty, odejmując rabat od całkowitej ceny

print(f"Number of products purchased: {amount}")  # Wypisuje liczbę zakupionych produktów
print(f"Product price: {base_price}")  # Wypisuje cenę produktu
print(f"Amount to pay: {amount_to_pay}")  # Wypisuje kwotę do zapłaty