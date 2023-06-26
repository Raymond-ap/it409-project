# Import required modules
import turtle


# 1.Developing a simple turtle Halloween animation in java or python or any programming language using
#  the following tags 

# # import required modules
# # Whole pumpkin
# # The turtle to "carve" the pumpkin
# # "Flatten" the lower part of the pumpkin
# # Make eyes
# # Make mouth
# # Make nose
# # Write text on animation

# Setup the turtle screen
screen = turtle.Screen()
screen.bgcolor("blue")
screen.title('Apungu Raymond - ADS20A00073Y')

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.shape("turtle")
pumpkin.color("orange")

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()
carver.shape("turtle")
carver.color("green")

# Draw the pumpkin
pumpkin.begin_fill()
pumpkin.circle(100)  # Adjust the circle size to change the pumpkin size
pumpkin.end_fill()

# Carve eyes
carver.penup()
carver.goto(-50, 30)  # Adjust the eye positions as per the pumpkin size
carver.pendown()
carver.color("black")
carver.begin_fill()
carver.circle(15)  # Adjust the circle size to change the eye size
carver.end_fill()

carver.penup()
carver.goto(50, 30)  # Adjust the eye positions as per the pumpkin size
carver.pendown()
carver.begin_fill()
carver.circle(15)  # Adjust the circle size to change the eye size
carver.end_fill()

# Carve mouth
carver.penup()
carver.goto(-60, -20)  # Adjust the mouth position as per the pumpkin size
carver.pendown()
carver.color("black")
carver.width(5)
carver.goto(-40, -60)  # Adjust the mouth shape as per the pumpkin size
carver.goto(40, -60)  # Adjust the mouth shape as per the pumpkin size
carver.goto(60, -20)  # Adjust the mouth shape as per the pumpkin size

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.goto(-100, -100)  # Adjust the position to start flattening the pumpkin
carver.pendown()
carver.color("orange")
carver.begin_fill()
carver.goto(100, -100)  # Adjust the position to end the flattening of the pumpkin
carver.goto(100, -150)  # Adjust the position to start the vertical line for flattening
carver.goto(-100, -150)  # Adjust the position to end the vertical line for flattening
carver.goto(-100, -100)  # Adjust the position to close the shape for flattening
carver.end_fill()

# Draw the stem
carver.penup()
carver.goto(0, 80)  # Adjust the stem position as per the pumpkin size
carver.pendown()
carver.color("green")
carver.width(10)
carver.goto(0, 120)  # Adjust the stem length as per the pumpkin size

# Write text on animation
text_writer = turtle.Turtle()
text_writer.penup()
text_writer.goto(0, -150)  # Adjust the text position as per the pumpkin size
text_writer.color("white")
text_writer.write("Happy Halloween!", align="center", font=("Arial", 15, "bold"))

# Hide the carver turtle
carver.hideturtle()

# Exit on click
turtle.done()
