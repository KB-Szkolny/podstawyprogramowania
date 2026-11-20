import re  # import modułu do wyrażeń regularnych, potrzebny do re.findall()
from decimal import Decimal  # import klasy Decimal do precyzyjnych obliczeń na kwotach bez błędów zaokrąglania

# Zadanie 3-4
# Raport zakupowy report.txt zawiera kwoty podane w euro.
email_file = "report.txt"

with open(email_file, "r", encoding="utf-8") as file:
    email = file.read()

# Wyrażenie regularne wyszukuje kwoty poprzedzone znakiem euro.
pattern = r"€\s*(\d+(?:[.,]\d{1,2})?)"
amounts = re.findall(pattern, email)
# Przecinek dziesiętny jest zamieniany na kropkę, a kwoty są sumowane bez błędów zaokrąglania.
total = sum((Decimal(amount.replace(",", ".")) for amount in amounts), Decimal("0"))

# Wynik przedstawia sumę z dokładnością do dwóch miejsc po przecinku.
print(f"Total spent: €{total:.2f}")
