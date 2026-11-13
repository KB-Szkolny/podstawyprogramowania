###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'  # Przypisuje wartość 'Krakow University of Economics' do zmiennej university, która przechowuje nazwę uczelni
university_expanded = ''  # Przypisuje pustą wartość do zmiennej university_expanded, która będzie przechowywać rozszerzoną nazwę uczelni

for char in university:  # Rozpoczyna pętlę, która iteruje przez każdy znak (char) w ciągu university
    university_expanded = university_expanded + char + ' '  # Do zmiennej university_expanded dodaje aktualny znak (char) oraz spację

print(university)  # Wypisuje oryginalną nazwę uczelni
print(university_expanded)  # Wypisuje rozszerzoną nazwę uczelni z dodatkowymi spacjami między znakami