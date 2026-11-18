###
# Unit conversion functions
#

def m_to_cm(n):
    return n * 100    # Przelicza metry na centymetry (1 m = 100 cm)

def cm_to_m(n):
    return n / 100   # Przelicza centymetry na metry (1 cm = 0.01 m)

def cm_to_inch(n):
    return n / 2.54        # Przelicza centymetry na cale (1 cal = 2.54 cm)

def feet_inch_to_cm(feet, inches):
    # 1 stopa = 12 cali (czyli 30.48 cm), 1 cal = 2.54 cm
    total_inches = (feet * 12) + inches   # Zamienia stopy i cale na łączną liczbę cali
    return total_inches * 2.54            # Mnoży łączną liczbę cali przez 2.54, dając centymetry