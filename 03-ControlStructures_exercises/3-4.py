###
# Checks whether at least one number entered
# from the keyboard is not negative
#
x = int(input('Enter first number: '))  # Wypisuje komunikat proszący użytkownika o wpisanie pierwszej liczby, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej x
y = int(input('Enter second number: '))  # Wypisuje komunikat proszący użytkownika o wpisanie drugiej liczby, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej y

if not x < 0 or not y < 0 :  # Sprawdza warunek: czy x NIE jest mniejsze niż 0 LUB y NIE jest mniejsze niż 0, czyli czy przynajmniej jedna z liczb jest nieujemna
    print(f'At least one of the numbers {x} and {y} is not negative')  # Jeśli warunek jest prawdziwy, wypisuje że przynajmniej jedna z liczb jest nieujemna
else:  # Jeśli warunek jest fałszywy, czyli obie liczby są ujemne
    print(f'Numbers {x} and {y} are negative')  # Wypisuje że obie liczby są ujemne