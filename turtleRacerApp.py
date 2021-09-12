import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
	racers = 0;

	while True:
		racers = input('Enter the number of racers (2 - 10): ')

		if racers.isdigit():
			racers = int(racers)
		else:
			print('Input is not numeric...Try Again!')
			continue

		if 2 <= racers <= 10:
			return racers;
		else:
			print('Number not in range 2 - 10. Try Again!')

def race(colors):
	turtles = create_turles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x,y = racer.pos()
			if y >= HEIGHT//2 - 10:
				return colors[turtles.index(racer)]

def create_turles(colors):
	turtles = []

	# double slash is an integer division, divides and keeps the whole number
	spacingx = WIDTH // (len(colors) + 1)

	# enumerate gives both the index and the value (i , color)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles


def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Turtle Racing!')


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner of the race is turtle:", winner)
time.sleep(5)

