###
# Functions to read any data type from the keyboard
#

def input_string(message):
    text = input(message)    # Pobiera tekst z klawiatury
    return text              # Zwraca ciąg znaków (str)

def input_integer(message):
    number = int(input(message))    # Pobiera tekst i konwertuje go na liczbę całkowitą
    return number            # Zwraca liczbę całkowitą (int)

def input_real(message):
    number = float(input(message))     # Pobiera tekst i konwertuje go na liczbę rzeczywistą (zmiennoprzecinkową)
    return number          # Zwraca liczbę rzeczywistą (float)

def input_boolean(message):
    answer = input(message)         # Pobiera odpowiedź z klawiatury (np. 'y' lub 'n')
    return answer.lower() == 'y'  # Zwraca True, jeśli wpisano 'y' (lub 'Y'), w przeciwnym razie False