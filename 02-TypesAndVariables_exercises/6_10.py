movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))  # Zlicza całkowitą liczbę znaków (wraz ze spacjami)

# print title in capital letters
print('Capital letters: ', movie.upper())   # Zamienia wszystkie litery na wielkie (.upper())

# print title in small letters
print('Small letters: ', movie.lower())   # Zamienia wszystkie litery na małe (.lower())

# print how many times the vowel "e" appears in the title
print('Count of "e": ', movie.count('e'))   # Zlicza wystąpienia litery 'e' (.count())

# print where in the text is the word "Lord"
print('Position of "Lord": ', movie.find('Lord'))   # Zwraca indeks pierwszego znaku słowa 'Lord'

# print where in the text is the word "dragon"
print('Position of "dragon": ', movie.find('dragon'))   # Zwraca -1, ponieważ słowo 'dragon' nie występuje w tekście