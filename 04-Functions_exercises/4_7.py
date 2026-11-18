###
# Converts letter to corresponding ICAO word
#
def icao(letter):
    letter = letter.capitalize()   # Zamienia wpisaną literę na wielką, aby działała niezależnie od wielkości znaków
    if letter == 'A':
        icao_name = 'Alfa'
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:
        icao_name = '???'  # Zabezpieczenie na wypadek znaków spoza alfabetu (np. spacji lub cyfr)

    return icao_name     # Zwraca dopasowane słowo z alfabetu ICAO

# Użycie funkcji do przeliterowania nazwy wpisanej z klawiatury
name = input('Enter your name: ')    # Pobiera słowo/imię od użytkownika
print('Spelled text:')

for char in name:            # Pętla pobiera kolejno każdą literę z wpisanego tekstu
    word = icao(char)           # Tłumaczy pojedynczą literę na słowo ICAO
    print(word, end=" ")       # Wypisuje słowo w jednej linii, oddzielając je spacją