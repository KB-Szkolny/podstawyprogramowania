# A program that prints your height both in cm and in feet and inches.

cm = 170                        # Wzrost w centymetrach

total_inches = round(cm / 2.54) # Przelicza centymetry na łączną liczbę całych cali (1 cal = 2.54 cm)
feet = total_inches // 12       # Oblicza pełne stopy (dzielenie całkowite //, 1 stopa = 12 cali)
inches = total_inches % 12      # Oblicza pozostałe cale (reszta z dzielenia modulo %)

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')  # Wypisuje wynik w obu systemach