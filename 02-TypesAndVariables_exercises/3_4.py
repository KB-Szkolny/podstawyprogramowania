speed_kmh = 70    # Przypisuje prędkość w kilometrach na godzinę (int)
speed_ms = speed_kmh / 3.6   # Przelicza km/h na m/s (1 m/s = 3.6 km/h), daje float

print(speed_kmh, "km/h = ", speed_ms, "m/s")  # Wypisuje wynik przeliczenia (70 km/h = 19.4444... m/s)