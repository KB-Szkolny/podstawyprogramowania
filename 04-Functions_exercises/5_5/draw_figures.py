###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# --- KWADRATY ---
# 1. Kwadrat (lewy górny róg)
pen.penup()
pen.goto(-200, 150)
pen.pendown()
figures.draw_square(pen, 80)

# 2. Kwadrat (prawy dolny róg)
pen.penup()
pen.goto(100, -100)
pen.pendown()
figures.draw_square(pen, 60)

# --- TRÓJKĄTY ---
# 1. Trójkąt (prawy górny róg)
pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_triangle(pen, 90)

# 2. Trójkąt (lewy dolny róg)
pen.penup()
pen.goto(-200, -150)
pen.pendown()
figures.draw_triangle(pen, 70)

# --- PROSTOKĄTY ---
# 1. Prostokąt (góra, środek)
pen.penup()
pen.goto(-50, 200)
pen.pendown()
figures.draw_rectangle(pen, 100, 50)

# 2. Prostokąt (dół, środek)
pen.penup()
pen.goto(-50, -50)
pen.pendown()
figures.draw_rectangle(pen, 120, 40)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()