name = 'Anna'     # Podstaw swoje imię
surname = 'May'   # Podstaw swoje nazwisko

characters_in_name = len(name)        # Oblicza liczbę znaków w imieniu
characters_in_surname = len(surname)  # Oblicza liczbę znaków w nazwisku

full_name = name + ' ' + surname       # Łączy imię i nazwisko ze spacją (np. 'Anna May')


characters_in_full_name = len(full_name)  # Oblicza liczbę znaków w pełnym imieniu i nazwisku (wraz ze spacją)

# Drukowanie wyników za pomocą f-strings
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_full_name} characters')