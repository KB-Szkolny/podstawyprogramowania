# Zadanie 1-9
# Plik it_company.csv zawiera listę pracowników.
employees_file = "it_company.csv"
job_title = "Software Engineer"

# Nagłówek jest pomijany, a każdy wiersz z danymi pracownika jest sprawdzany.
with open(employees_file, "r", encoding="utf-8") as file:
    next(file, None)
    number = 0
    for line in file:
        # Osoby na wybranym stanowisku są wypisywane i numerowane.
        if job_title in line:
            number += 1
            print(f"{number}. {line.rstrip()}")
