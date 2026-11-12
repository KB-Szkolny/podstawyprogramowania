total = 8000000000       # Całkowita populacja Ziemi (int)
north = 7200000000        # Populacja półkuli północnej (int)
south = total - north  # Oblicza populację półkuli południowej (8000000000 - 7200000000 = 800000000)

print("World population: ", total)      # Wypisuje całkowitą populację
print("Northern Hemisphere: ", north)   # Wypisuje populację półkuli północnej

# Oblicza i wypisuje procentowy udział półkuli północnej 
print("Northern Hemisphere in %: ", north / total * 100)

print("Southern Hemisphere: ", south)   # Wypisuje populację półkuli południowej

# Oblicza i wypisuje procentowy udział półkuli południowej 
print("Southern Hemisphere in %: ", south / total * 100)