
# Program for testing built-in functions

# Największa liczba z zestawu
max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7,5,6,3,8,2 is', max_number)

# Najmniejsza liczba z zestawu
min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4,7,2,3,9,8 is', min_number)

# Długość frazy "computer science" 
str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

# Znak/tekst odczytany z klawiatury ("Pismo odczytywane z klawiatury" to tłumaczenie "letter read from the keyboard")
letter = input('Enter a letter: ')
print('Letter read from the keyboard is', letter)

# Liczba reprezentująca ciąg "20303"
number_from_str = int("20303")
print('Number representing string "20303" is', number_from_str)

# Ciąg binarny ("ciąg podwójny" = binary string) reprezentujący liczbę 304
binary_str = bin(304)
print('Binary string representing 304 is', binary_str)

# Ciąg szesnastkowy reprezentujący liczbę 304
hex_str = hex(304)
print('Hexadecimal string representing 304 is', hex_str)

# Liczba całkowita reprezentująca kod Unicode znaku €
unicode_euro = ord('€')
print('Unicode code for € is', unicode_euro)

# Wartość bezwzględna z -17
abs_value = abs(-17)
print('Absolute value of -17 is', abs_value)