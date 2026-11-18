###
# Module with functions for drawing geometric figures
#

def draw_square(pen, length):
    for i in range(4):     # Rysuje 4 boki kwadratu
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    for i in range(3):      # Rysuje 3 boki trójkąta równobocznego
        pen.forward(length)
        pen.left(120)   # Obrót o 120 stopni tworzy kąty wewnętrzne 60 stopni

def draw_rectangle(pen, length_a, length_b):
    for i in range(2):    # Powtarza 2 razy parę boków (a i b)
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)