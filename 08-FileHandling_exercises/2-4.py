# Zadanie 2-4
# Plik it_company.csv zawiera pracowników; wyniki trafią do osobnego pliku.
employees_file = "it_company.csv"
position_file = "software_engineer.txt"
job_title = "Software Engineer"

# Do pliku wynikowego trafiają tylko pasujący pracownicy.
with open(employees_file, "r", encoding="utf-8") as source:
    with open(position_file, "w", encoding="utf-8") as destination:
        for line in source:
            if job_title in line:
                destination.write(line)

# Komunikat podaje nazwę pliku z wynikami.
print(f"Selected employees saved to {position_file}.")
