height = input('Enter your height in cm: ')     # Pobiera wzrost w cm jako tekst 
weight = input('Enter your weight in kg: ')     # Pobiera wagę w kg jako tekst 

height = int(height)       # Konwertuje tekst ze wzrostem na liczbę całkowitą 
weight = int(weight)      # Konwertuje tekst z wagą na liczbę całkowitą 

bmi = weight / (height / 100) ** 2     # Oblicza BMI ze wzoru: waga / (wzrost w metrach)^2
bmi = round(bmi, 2)         # Zaokrągla wynik BMI do 2 miejsc po przecinku

print('Your BMI is', bmi)      # Wypisuje wyliczone BMI
print('Check on the Internet if your BMI is ok!!') # Wyświetla informację o sprawdzeniu wyniku