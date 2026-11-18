###
# Tests functions from the converters module
#
import converters      # Importuje stworzony przez Ciebie moduł converters.py

if __name__ == "__main__":
    # Testy istniejących funkcji
    print(f'2m = {converters.m_to_cm(2)}cm')
    print(f'532cm = {converters.cm_to_m(532)}m')
    
    # Testy nowych funkcji
    print(f'100cm = {converters.cm_to_inch(100):.2f} inches')
    print(f'5 feet 10 inches = {converters.feet_inch_to_cm(5, 10):.2f}cm')