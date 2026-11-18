import turtle  # Import modułu graficznego

def draw_square(length):        # Funkcja rysująca kwadrat o boku 'length'
    pen = turtle.Turtle()        # Utworzenie żółwia
    pen.speed(5)                 # Ustawienie prędkości rysowania

    for i in range(4):           # Rysowanie 4 boków
        pen.forward(length)      # Ruch do przodu
        pen.right(90)           # Obrót o 90 stopni

    pen.hideturtle()            # Ukrycie żółwia