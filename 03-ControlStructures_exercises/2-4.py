###  # Nagłówek sekcji kodu
# Simple calculator  # Nagłówek opisujący cel programu: prosty kalkulator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.
#
number1 = float(input('First number: '))  # Wypisuje komunikat proszący użytkownika o wpisanie pierwszej liczby, pobiera wpisany tekst, konwertuje go na liczbę zmiennoprzecinkową i przypisuje do zmiennej number1
number2 = float(input('Second number: '))  # Wypisuje komunikat proszący użytkownika o wpisanie drugiej liczby, pobiera wpisany tekst, konwertuje go na liczbę zmiennoprzecinkową i przypisuje do zmiennej number2
operator = input('Operator [+, -, *, /]: ')  # Wypisuje komunikat proszący użytkownika o wpisanie operatora i przypisuje wpisany tekst do zmiennej operator

if operator == '+':  # Sprawdza warunek: czy operator jest równy '+'
    result = number1 + number2  # Jeśli warunek jest prawdziwy, dodaje number1 do number2 i przypisuje wynik do zmiennej result
elif operator == '-':  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy operator jest równy '-'
    result = number1 - number2  # Jeśli warunek jest prawdziwy, odejmuje number2 od number1 i przypisuje wynik do zmiennej result
elif operator == '*':  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy operator jest równy '*'
    result = number1 * number2  # Jeśli warunek jest prawdziwy, mnoży number1 przez number2 i przypisuje wynik do zmiennej result
elif operator == '/':  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy operator jest równy '/'
    result = number1 / number2  # Jeśli warunek jest prawdziwy, dzieli number1 przez number2 i przypisuje wynik do zmiennej result
else:  # Jeśli żaden z powyższych warunków nie jest prawdziwy, czyli operator jest niepoprawny
    print('Wrong operator')  # Wypisuje komunikat o niepoprawnym operatorze

# print result  # Wypisanie wyniku
print(f'{number1} {operator} {number2} = {result}')  # Wypisuje pierwszą liczbę, operator, drugą liczbę i wynik operacji