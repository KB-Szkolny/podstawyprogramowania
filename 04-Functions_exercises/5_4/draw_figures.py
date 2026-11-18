import turtle                       # Import modułu graficznego

# Set up the screen
window = turtle.Screen()        # Utworzenie okna ekranu
window.bgcolor("lightgreen")     # Ustawienie koloru tła na jasnozielony

# Create the turtle
pen = turtle.Turtle()            # Utworzenie żółwia (pióra)
pen.speed(5)                     # Ustawienie prędkości rysowania

# Side length
side_length = 100       # Długość boku kwadratu

# Draw a square
for i in range(4):                # Pętla wykonująca się 4 razy
    pen.forward(side_length)     # Ruch do przodu o długość boku
    pen.right(90)                # Obrót w prawo o 90 stopni

# Hide the turtle and finish
pen.hideturtle()             # Ukrycie ikony żółwia
window.mainloop()            # Utrzymanie okna otwartego
