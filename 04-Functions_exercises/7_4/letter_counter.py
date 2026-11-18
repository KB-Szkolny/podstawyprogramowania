def count_letter(text, letter):          # Definicja funkcji zliczającej wystąpienia danej litery w tekście
    return text.count(letter)           # Metoda count() zwraca liczbę wystąpień znaku w napisie

if __name__ == "__main__":              # Kod testowy przy bezpośrednim uruchomieniu modułu
    print(count_letter("test", "t"))    # Wynik testu: 2