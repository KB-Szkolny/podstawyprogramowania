previous_price = 200.00  # Przypisuje wartość 200.00 do zmiennej previous_price, która przechowuje poprzednią cenę produktu
current_price = float(input("Enter current product price: "))  # Wypisuje komunikat proszący użytkownika o wpisanie aktualnej ceny produktu, pobiera wpisany tekst, konwertuje go na liczbę zmiennoprzecinkową i przypisuje do zmiennej current_price
discount = ((previous_price - current_price) / previous_price) * 100  # Oblicza procentową obniżkę ceny, odejmując aktualną cenę od poprzedniej, dzieląc przez poprzednią cenę i mnożąc przez 100
if current_price < (previous_price * 0.9):  # Sprawdza warunek: czy aktualna cena (current_price) jest mniejsza niż 90% poprzedniej ceny (previous_price * 0.9), czyli czy obniżka wynosi więcej niż 10%
    print("Buy the product!!")  # Jeśli warunek jest prawdziwy, wypisuje zachętę do zakupu produktu
    print(f"Product price reduced by {discount}%")  # Wypisuje procentową obniżkę ceny produktu