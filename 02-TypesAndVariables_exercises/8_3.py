celsius = float(input('Enter temperature in Celsius: '))  # Pobiera temperaturę w stopniach Celsjusza i zamienia na liczbe zmiennoprzecinkową

kelvin = celsius + 273.15                                 # Przelicza Celsjusze na Kelwiny
fahrenheit = (celsius * 9 / 5) + 32                       # Przelicza Celsjusze na Fahrenheity

print(f'Temperature in Celsius: {celsius}°C')             # Wypisuje temperaturę w Celsjuszach
print(f'Temperature in Kelvin: {kelvin} K')               # Wypisuje temperaturę w Kelwinach
print(f'Temperature in Fahrenheit: {fahrenheit}°F')       # Wypisuje temperaturę w Fahrenheitach