import turtle
import random

# Load required modules
screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(width=800, height=600)
colors = ["red", "blue", "green", "yellow"]

# Create racing track
track = turtle.Turtle()
track.penup()
track.goto(-350, 200)
track.pendown()
track.goto(-350, -200)
track.penup()
track.hideturtle()

# Define a function for the 360-degree turn
def turn_around(t):
    t.right(360)

# Define a function to gradually start the race
def start_race(t, speed):
    while t.xcor() < 350:
        t.forward(speed)

# First player details
player1_name = "Player 1"
player1 = turtle.Turtle(shape="turtle")
player1.color(colors[0])
player1.penup()
player1.goto(-380, 170)

# Show first player details
player1_details = f"Name: {player1_name}"
player1_details += f"\nColor: {colors[0]}"
player1_details += f"\nSpeed: {player1.speed()}"
player1.write(player1_details, align="left", font=("Arial", 12, "normal"))

# First player makes a 360-degree turn
turn_around(player1)

# Second player details
player2_name = "Player 2"
player2 = turtle.Turtle(shape="turtle")
player2.color(colors[1])
player2.penup()
player2.goto(-380, 90)

# Show second player details
player2_details = f"Name: {player2_name}"
player2_details += f"\nColor: {colors[1]}"
player2_details += f"\nSpeed: {player2.speed()}"
player2.write(player2_details, align="left", font=("Arial", 12, "normal"))

# Second player makes a 360-degree turn
turn_around(player2)

# Third player details
player3_name = "Player 3"
player3 = turtle.Turtle(shape="turtle")
player3.color(colors[2])
player3.penup()
player3.goto(-380, 10)

# Show third player details
player3_details = f"Name: {player3_name}"
player3_details += f"\nColor: {colors[2]}"
player3_details += f"\nSpeed: {player3.speed()}"
player3.write(player3_details, align="left", font=("Arial", 12, "normal"))

# Third player makes a 360-degree turn
turn_around(player3)

# Fourth player details
player4_name = "Player 4"
player4 = turtle.Turtle(shape="turtle")
player4.color(colors[3])
player4.penup()
player4.goto(-380, -70)

# Show fourth player details
player4_details = f"Name: {player4_name}"
player4_details += f"\nColor: {colors[3]}"
player4_details += f"\nSpeed: {player4.speed()}"
player4.write(player4_details, align="left", font=("Arial", 12, "normal"))

# Fourth player makes a 360-degree turn
turn_around(player4)

# Start the race for all players together
speeds = [random.randint(1, 10) for _ in range(4)]
start_race(player1, speeds[0])
start_race(player2, speeds[1])
start_race(player3, speeds[2])
start_race(player4, speeds[3])

turtle.done()
