father_income = 5450             # Dochód ojca (int)
mother_income = 4920            # Dochód matki (int)
family_members = 5               # Liczba członków rodziny (int)

total_income = father_income + mother_income    # Oblicza łączny dochód rodziny
income_per_person = total_income / family_members   # Oblicza dochód na osobę:

# Wypisuje całkowity dochód oraz dochód przypadający na jedną osobę z użyciem f-stringa
print(f'Total family income is {total_income}, and income per person is {income_per_person}')