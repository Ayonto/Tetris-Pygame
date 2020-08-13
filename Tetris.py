# made by _S_I_Ayonto
# 2020

import pygame
import types
import time
from Block import Block
pygame.init()

# Board
Board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #3
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #8
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #9
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #10
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #11
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #12
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #13
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #14
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #15
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #16
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #17
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #18
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #19
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #21

# setting up display

WIDTH, HEIGHT = (400, 601)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris!")

# colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (155, 155, 155)
# variables 
block = Block()
block.spawn()

score = 0

# fonts
comicsams = pygame.font.SysFont("comicsams", 32)
Title = pygame.font.SysFont("comicsams", 48)
# functions

def collision(x, y):
	for j in block.Block_list:
		for i in j:
			if not isinstance(i, bool) and i != j[-1]:
				if i[0] == x and i[1] == y+1:
					return True
	return False
			

def checkLastBlock():
	for i in block.Block_list[-1]:
		if i[-1] == False:
			return True
		else: return False


def pop_block(y):
	for _ in range(10):
		for j in block.Block_list:
			for i in j:
				if not isinstance(i, bool) and i != j[-1]:
					if i[1] == y:
						j.pop(j.index(i))
					
	# for j in block.Block_list:
	# 	for i in range(len(j)):
	# 		if not isinstance(j[i], bool):
	# 			if j[i][1] == y:
	# 				j.pop(i)
	# 				i = 0


def move_down(y):
	for j in block.Block_list:
		for i in j:
			if not isinstance(i, bool) and i!=j[-1] and i[1]<y:
				i[1] += 1

def printBoard():   # for debug purpose
	for i in Board:
		print(i)

def checkBlockPosition(n, m):
	for y in block.Block_list:
		for x in y:
			# print(f"x, y = {x[0], x[1]}")
			# print(x)
			# print(f"n, m = {n, m}")
			if not isinstance(x, bool) and x != y[-1]:
				if x[0] == n and x[1] == m:
					return True
	return False

def check_lost():
	for j in block.Block_list:
		for i in j:
			if not isinstance(i, bool) and i != j[-1]:
				if i[1] == 0:
					return True
	return False

def updateBoard():
	for j in range(20):
		for i in range(10):
			if checkBlockPosition(i, j) == True:
				Board[j][i] = 1
			if checkBlockPosition(i, j) == False:
				Board[j][i] = 0


def draw_grid():
	# verticle line
	for v in range(0, 11):
		pygame.draw.line(window, gray, ((v*3)*10, 0), ((v*3)*10, 600))
	# horizontal line
	for h in range(0, 21):
		pygame.draw.line(window, gray, (0, (h*3)*10), (300, (h*3)*10))
def draw():
	window.fill(black)
	# draw_grid()

	# drawing blocks
	for j in block.Block_list:
		for i in j:
			if not isinstance(i, bool) and i != j[-1]:
				pygame.draw.rect(window, j[-1], ((i[0]*3)*10, (i[1]*3)*10, 30, 30))

	# drawing fonts
	Tetris_font = Title.render("Tetris", 1, white)

	score_font = comicsams.render(f"{str(score)}", 1, white)

	window.blit(Tetris_font, (350-Tetris_font.get_width()/2, 15))
	window.blit(score_font, (350-score_font.get_width()/2, 200))

	draw_grid()

	pygame.display.update()

# events
running = True

start_tick = pygame.time.get_ticks()
move_time = 0.4
# game loop
while running:
	timer = (pygame.time.get_ticks()-start_tick)/1000
	if timer > move_time:
		for j in block.Block_list:
			if j[-2] == True:
				for i in j:
					if not isinstance(i, bool) and i!=j[-1]:
					# moving the block
						if i[1] < 19:
							i[1] += 1
							start_tick = pygame.time.get_ticks()
						if i[1] == 19 or collision(i[0], i[1])==True:
							j[-2] = False


	if block.Block_list[-1][-2] == False:
		block.lastOneDone = True
	else: block.lastOneDone = False
	

	if(block.lastOneDone == True):
		block.lastOneDone = False
		block.spawn()



	draw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				move_time = 0.2
			if event.key == pygame.K_RIGHT:
				for i in block.Block_list[-1]:
					if not isinstance(i, bool) and i != block.Block_list[-1][-1]:
						i[0] += 1
			if event.key == pygame.K_LEFT:
				for i in block.Block_list[-1]:
					if not isinstance(i, bool) and i != block.Block_list[-1][-1]:
						i[0] -= 1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				move_time = 0.6

	if block.lastOneDone == True:
		block.spawn()
		block.lastOneDone = False

	# updating the board
	updateBoard()

	# checking for row completion
	time.sleep(0.1)
	for j in range(len(Board)):
		if all(n==1 for n in Board[j]) == True and block.Block_list[-2][-2] == False:
			print(f"{j} Row is same")
			pop_block(j)
			move_down(j)
			score += 1

	# check for lost

	if(check_lost()==True):
		pass


	

pygame.quit()
printBoard()