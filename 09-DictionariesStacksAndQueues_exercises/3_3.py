import queue

def brackets_ok(expression):
    stack = queue.LifoQueue()
    # Słownik ułatwiający sprawdzenie, jaki nawias otwierający pasuje do danego zamykającego
    matching_brackets = {')': '(', '}': '{', ']': '['}

    # Przechodzimy znak po znaku przez całe wyrażenie matematyczne
    for char in expression:
        if char in "({[":
            # Każdy napotkany nawias otwierający odkładamy na stos (czeka na swoją parę)
            stack.put(char)
        elif char in ")}]":
            # Gdy trafiamy na nawias zamykający, ale stos jest pusty – brakuje nawiasu otwierającego
            if stack.empty():
                return False
            
            # Zdejmujemy ze stosu ostatni otwarty nawias i sprawdzamy, czy pasuje typem do zamykającego
            top = stack.get()
            if top != matching_brackets[char]:
                return False            # Np. otwarto '(', a zamknięto ']' – błąd składni

    # Jeśli po sprawdzeniu całego wyrażenia stos jest pusty, wszystkie nawiasy miały swoje pary
    # Gdyby coś na nim zostało (np. niedomknięty nawias), .empty() zwróci False
    return stack.empty()

def main():
    expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # nawiasy poprawne
    expression2 = "[(2+3]/4)"                  # nawiasy niepoprawne
    expression3 = "(2-3*4+(5/6)"               # nawiasy niepoprawne

    # Testujemy każde z trzech wyrażeń i wypisujemy wynik
    for i, expr in enumerate([expression1, expression2, expression3], start=1):
        if brackets_ok(expr):
            print(f"Expression {i} ({expr}): Brackets are OK")
        else:
            print(f"Expression {i} ({expr}): Brackets are NOT correct")

if __name__ == "__main__":
    main()