###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20  # Przypisuje wartość 20 do zmiennej total_tasks, która przechowuje całkowitą liczbę zadań
tasks_ok = int(input('Wprowadz liczbe dobrze wykonanych zadan: '))  # Wypisuje komunikat proszący użytkownika o wpisanie liczby dobrze wykonanych zadań, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej tasks_ok
test_passed = False  # Przypisuje wartość False do zmiennej test_passed, która oznacza, że test nie został zdany

if tasks_ok >= total_tasks/2 :  # Sprawdza warunek: czy liczba poprawnie wykonanych zadań (tasks_ok) jest większa lub równa połowie całkowitej liczby zadań (total_tasks/2)
    test_passed = True  # Jeśli warunek jest prawdziwy, przypisuje wartość True do zmiennej test_passed, oznaczając że test został zdany

if test_passed:  # Sprawdza warunek: czy zmienna test_passed ma wartość True
    print('Congratulations! You passed the test.')  # Jeśli warunek jest prawdziwy, wypisuje gratulacje za zdanie testu
else:  # Jeśli warunek (test_passed) jest fałszywy, czyli test nie został zdany
    print('Unfortunately, you failed the test.')  # Wypisuje komunikat o nieudanym teście