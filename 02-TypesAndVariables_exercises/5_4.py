# Używamy float(), aby obsłużyć kwoty z ułamkiem/groszami
amount = float(input('Enter amount: '))

# Wzory na kwotę netto i podatek VAT (przy stawce 23% w brutto)
vat = amount * (23 / 123)

print(f"Amount  : {amount:>5.2f}")  # Wypisuje pobraną kwotę: wyrównaną do prawej (szerokość min. 5 znaków), 2 miejsca po przecinku
print(f"VAT 23% : {vat:>5.2f}")      # Wypisuje obliczony podatek VAT: wyrównany do prawej, zaokrąglony do 2 miejsc po przecinku
