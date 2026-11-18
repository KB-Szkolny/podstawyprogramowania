
# To use the functions available in an external module,
# you must include that module in your program.
import math

# Pierwiastek kwadratowy z 7
square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

# Logarytm naturalny z 5
natural_log = math.log(5)
print('A natural logarithm of 5 is', natural_log)

# Sinus 90 stopni (funkcja math.sin() wymaga kątów w radianach, dlatego konwertujemy 90° za pomocą math.radians())
sine_90 = math.sin(math.radians(90))
print('A sine of 90 degrees is', sine_90)