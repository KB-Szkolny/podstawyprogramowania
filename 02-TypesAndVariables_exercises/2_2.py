1. 3 * 2 + 1
    Argumenty (3): 3, 2, 1
    Operatorzy (2): *, +
    Obliczenia: Najpierw mnożenie 3 * 2 = 6, potem dodawanie 6 + 1 = 7.
    Wynik: 7

2. 5 + 10 * 5
    Argumenty (3): 5, 10, 5
    Operatorzy (2): +, *
    Obliczenia: Najpierw mnożenie 10 * 5 = 50, potem dodawanie 5 + 50 = 55.
    Wynik: 55

3. 4 + 4 / 2 ** 2
    Argumenty (4): 4, 4, 2, 2
    Operatorzy (3): +, /, **
    Obliczenia:
        Potęgowanie: 2 ** 2 = 4
        Dzielenie: 4 / 4 = 1.0 (w Pythonie dzielenie / zawsze zwraca typ zmiennoprzecinkowy float)
        Dodawanie: 4 + 1.0 = 5.0
    Wynik: 5.0

4. 4 % 3 % 2 % 1
    Argumenty (4): 4, 3, 2, 1
    Operatorzy (3): %, %, %
    Obliczenia: Operator % (modulo - reszta z dzielenia) wiąże od lewej do prawej:
        4 % 3 = 1 (bo 4 = 1 * 3 + reszta 1)
        1 % 2 = 1 (bo 1 = 0 * 2 + reszta 1)
        1 % 1 = 0 (bo 1 = 1 * 1 + reszta 0)
    Wynik: 0

5. 1 + 2 % 3 ** 4 * 5
    Argumenty (5): 1, 2, 3, 4, 5
    Operatorzy (4): +, %, **, *
    Obliczenia:
        Potęgowanie (najwyższy priorytet): 3 ** 4 = 81
        Modulo i mnożenie mają ten sam priorytet, wykonujemy od lewej:
            2 % 81 = 2 (reszta z dzielenia 2 przez 81 to 2)
            2 * 5 = 10
        Dodawanie na końcu: 1 + 10 = 11
    Wynik: 11

6. Prawda! = Fałszywe (w oryginalnym kodzie Pythona: True != False)
    Operatorzy (1): != (różne od)
    Obliczenia: Pytamy, czy wartość True jest różna od False. Ponieważ są to dwie różne wartości, odpowiedź brzmi "tak".
    Wynik: True