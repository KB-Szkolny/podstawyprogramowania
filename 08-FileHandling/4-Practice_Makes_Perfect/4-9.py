# Zadanie 4-9
# Plik it_company.csv zawiera dane pracowników.
employees_file = "it_company.csv"

# Nagłówek opisuje listę projektantów.
print("GRAPHIC DESIGNERS")
print("=================")

# Wiersze są odczytywane z użyciem nazw kolumn z nagłówka CSV.
with open(employees_file, "r", encoding="utf-8", newline="") as file:
    for employee in csv.DictReader(file):
        # Na liście pozostają tylko osoby pracujące jako Graphic Designer.
        if employee["Job Title"] == "Graphic Designer":
            # Wynik zawiera imię, nazwisko i adres e-mail w tej kolejności.
            print(
                f'{employee["First Name"]},'
                f'{employee["Last Name"]},'
                f'{employee["Email"]}'
            )
