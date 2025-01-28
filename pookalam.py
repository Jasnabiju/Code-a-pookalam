import turtle

import math



# Setup the window screen

window = turtle.Screen()

window.bgcolor('black')

window.setup(width=800, height=800)  # Set window size



# Create a turtle for drawing the Pookalam

t = turtle.Turtle()

t.speed(0)  # Fastest drawing



# Function to draw multiple shrinking circles with adjustable pen size and color

def Circles(t, size, color, width=1):

    for i in range(10):

        t.color(color)  # Set the color of the turtle

        t.pensize(width)  # Set pen size for the circle

        t.circle(size)

        size = size - 4



# Function to repeat circle patterns in a spirograph-like design

def drawCircles(t, size, repeat, color, width=1):

    for i in range(repeat):

        Circles(t, size, color, width)  # Pass the color to the Circles function

        t.right(360 / repeat)



# Function to draw filled circles

def draw_circle(radius, color):

    t.penup()

    t.goto(0, -radius)

    t.setheading(0)  # Ensure heading is reset

    t.pendown()

    t.fillcolor(color)

    t.begin_fill()

    t.circle(radius)

    t.end_fill()



# Function to draw sector pattern with alternating colors

def draw_sector_pattern(radius, sectors, color1, color2, line_color):

    angle = 360 / sectors

    t.penup()

    t.goto(0, -radius)

    t.setheading(0)  # Ensure turtle is facing up

    t.pendown()

    for i in range(sectors):

        t.fillcolor(color1 if i % 2 == 0 else color2)

        t.begin_fill()

        t.pencolor(line_color)

        t.circle(radius, extent=angle)

        position = t.pos()

        t.goto(0, 0)

        t.end_fill()

        t.setpos(position)



# Function to draw petals where tips align with sector lines

def draw_petals_with_alignment(radius, num_petals, petal_length, color):

    angle = 360 / num_petals

    t.fillcolor(color)

    for i in range(num_petals):

        t.penup()

        t.goto(0, 0)

        t.setheading(90 - (i * angle))  # Start angle offset

        t.forward(radius)

        t.pendown()

        t.begin_fill()

        t.left(30)

        t.circle(petal_length, 60)  # First curve of petal

        t.left(120)

        t.circle(petal_length, 60)  # Second curve of petal

        t.left(30)  # Re-adjust

        t.end_fill()



# Function to draw regular petals

def draw_petals(radius, num_petals, petal_size, color):

    angle = 360 / num_petals

    t.fillcolor(color)

    for _ in range(num_petals):

        t.begin_fill()

        t.circle(petal_size, extent=60)

        t.left(120)

        t.circle(petal_size, extent=60)

        t.left(60 + angle - 120)

        t.end_fill()



# Function to move to a specific location without drawing

def move_to(x, y):

    t.penup()

    t.goto(x, y)

    t.pendown()



# Function to draw the Pookalam

def draw_pookalam():

    # 1st Circle (Green, Radius 300)

    drawCircles(galatic, 155, 10, "green", 10)



    # 2nd Circle (12 sectors, alternate Orange and Yellow, Green lines, Radius 290)

    draw_sector_pattern(290, 12, "orange", "yellow", "green")



    # 4th layer (Smaller Violet Petals, overlapping the 3rd layer)

    t.penup()

    t.goto(0, 0)

    t.pendown()

    draw_petals(35, 12, 278, "green")



    # Re-center turtle to maintain concentricity

    t.penup()

    t.goto(0, 0)

    t.setheading(0)



    # 5th layer (12 Green Petals between 3rd petals)

    draw_petals(28, 12, 260, "blue")



    # Re-center turtle to maintain concentricity

    t.penup()

    t.goto(0, 0)

    t.setheading(0)



    # 6th layer (12 smaller White Petals overlapping the 5th)

    draw_petals(20, 12, 230, "violet")



    # Re-center turtle to maintain concentricity

    t.penup()

    t.goto(0, 0)

    t.setheading(0)



    # 7th layer (Green petals smaller than the 6th, overlapping)

    draw_petals(15, 12, 210, "white")



    # Re-center turtle before drawing the inner circles

    t.penup()

    t.goto(0, 0)

    t.setheading(0)



    # 8th Circle (Green, Radius 150)

    draw_circle(150, "green")



    # 9th Circle (Yellow, Radius 140)

    draw_circle(140, "yellow")



    # 10th Circle (Green, Radius 130)

    draw_circle(130, "green")



    # 11th Circle (Green, Radius 120)

    draw_circle(120, "green")



# 12th,13th,14th layers: Galactic Flower design

galatic = turtle.Turtle()

galatic.speed(0)



# Draw the Pookalam

draw_pookalam()



# Call the function to draw the galactic flower spirograph

drawCircles(galatic, 55, 10, "yellow", 10)

drawCircles(galatic, 40, 10, "orange", 10)

drawCircles(galatic, 1, 10, "red", 10)



#15th layer

t.penup()

t.goto(0, 0)

t.pendown()

draw_petals(50, 12, 50, "green")



#16th layer:

draw_circle(5, "blue")



# Complete the drawing

t.hideturtle()

galatic.hideturtle()

turtle.done()
