
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed

import keyboard     # Importuje moduł keyboard.py 

# Odczytuje dane pracownika z klawiatury za pomocą funkcji z modułu keyboard
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')

# Wypisuje kartotekę pracownika
print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)

# Sprawdza, czy wynagrodzenie NIE jest ukryte (not is_salary_hidden)
if not is_salary_hidden:
    print('Salary:', salary)