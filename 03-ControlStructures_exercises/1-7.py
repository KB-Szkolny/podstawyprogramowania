###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000  # Przypisuje wartość 5000 do zmiennej basic_salary, która przechowuje podstawową pensję
total_salary = 0  # Przypisuje wartość 0 do zmiennej total_salary, która będzie przechowywać całkowitą pensję
bonus = 0.3  # Przypisuje wartość 0.3 do zmiennej bonus, która oznacza stawkę bonusu (30%)
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'  # Wypisuje komunikat pytający czy pracownik otrzymuje bonus, pobiera odpowiedź użytkownika i sprawdza czy jest równa 'Y', przypisując wynik (True/False) do zmiennej is_bonus

if is_bonus:  # Sprawdza warunek: czy zmienna is_bonus ma wartość True, czyli czy pracownik otrzymuje bonus
    total_salary = basic_salary+(basic_salary*bonus)  # Jeśli warunek jest prawdziwy, oblicza całkowitą pensję jako sumę podstawowej pensji i bonusu (basic_salary * bonus)
else:  # Jeśli warunek (is_bonus) jest fałszywy, czyli pracownik nie otrzymuje bonusu
    total_salary = basic_salary  # Przypisuje do całkowitej pensji wartość podstawowej pensji bez bonusu

print(f'Basic salary: {basic_salary}')  # Wypisuje podstawową pensję
print(f'Bonus included? {is_bonus}')  # Wypisuje czy bonus został uwzględniony (True/False)
print(f'Total salary: {total_salary}')  # Wypisuje całkowitą pensję