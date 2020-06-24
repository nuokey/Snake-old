import pgzrun
from random import randint as rnd
from time import sleep

box_size = 36
box_number = 20

TITLE = "SNAKE | by NuoKey"
WIDTH = box_size * box_number
HEIGHT = box_size * box_number

# Variables
x = []
y = []
snake = [[10, 10], [9, 10], [8, 10]]
snake_speed = 0.4
vx = 1
vy = 0
food_pos = [rnd(0, 19), rnd(0, 19)]
food = Actor("food", topleft=(food_pos[0] * box_size, food_pos[1] * box_size))
score = 0

def draw_map():
	global box_size, box_number
	for cx in range(box_number):
		for cy in range(box_number):
			box = Rect((cx * box_size, cy * box_size), (cx * box_size + box_size, cy * box_size + box_size))
			if cx % 2 == 0 and cy % 2 == 0 or cx % 2 == 1 and cy % 2 == 1:
				box_color = (173, 216, 230)
			else:
				box_color = (176, 224, 230)
			screen.draw.filled_rect(box, box_color)

def draw_snake():
	global snake, box_size
	for s in range (len(snake)):
		if s == 0:
			actor = "top_snake"
		else:
			actor = "snake"
		Actor(actor, topleft=(snake[s][0] * box_size, snake[s][1] * box_size)).draw()

def up():
	global vx, vy
	vx = 0
	vy = -1

def down():
	global vx, vy
	vx = 0
	vy = 1

def left():
	global vx, vy
	vx = -1
	vy = 0

def right():
	global vx, vy
	vx = 1
	vy = 0

def snake_move():
	for s in range(len(snake)-1, -1, -1):
		if s != 0:
			snake[s][0] = snake[s-1][0]
			snake[s][1] = snake[s-1][1]
		else:
			snake[s][0] += vx
			snake[s][1] += vy
	clock.unschedule(snake_move)

def snake_angle():
	if keyboard.up:
		up()
	if keyboard.down:
		down()
	if keyboard.left:
		left()
	if keyboard.right:
		right()

def food_add():
	global food, food_pos, score, snake_speed, snake
	if snake[0][0] == food_pos[0] and snake[0][1] == food_pos[1]:
		snake.append(food_pos) 
		food_pos = [rnd(0, 19), rnd(0, 19)]
		food = Actor("food", topleft=(food_pos[0] * box_size, food_pos[1] * box_size))
		score += 1
		if snake_speed > 0.2:
			snake_speed -= 0.05

def game_end():
	global score
	screen.draw.text("End\nYour score: "+str(score), (WIDTH // 2, HEIGHT // 2))
	sleep(5)
	exit()

def collision():
	global snake
	if snake[0][0] > box_number -1 or snake[0][0] < 0 or snake[0][1] > box_number -1 or snake[0][1] < 0:
		game_end()
	for i in range (1, len(snake)-1):
		if snake[i] == snake[0]:
			game_end()

def draw():
	global score, food
	screen.clear()
	draw_map()
	draw_snake()
	food.draw()
	screen.draw.text("Score: "+str(score), topleft=(0, 0), fontsize=40, color="black")

def update():
	snake_angle()
	clock.schedule(snake_move, snake_speed)
	food_add()
	collision()

pgzrun.go()
