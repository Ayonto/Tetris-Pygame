import math
import random
class Block:
	def __init__(self):
		self.Block_list = []
		self.lastOneDone = False
	def spawn(self):
		random_choice = random.randint(0, 6)
		block_design = [[[3, 0], [3, 1], [4, 1], [5, 1], True, [0, 0, 255]], [[3, 0], [4, 0], [5, 0], [6, 0], True, [0, 255, 255]], [[3, 0], [3, 1], [4, 0], [4, 1], True, [255, 255, 0]],
						[[3, 0], [4, 0], [4, 1], [5, 1], True, [255, 0, 0]], [[5, 0], [4, 0], [4, 1], [3, 1], True, [0, 255, 0]], [[3, 0], [4, 0], [5, 0], [4, 1], True, [170, 0, 255]], [[5, 0], [5, 1], [4, 1], [3, 1], True, [255, 165, 0]]]

		# print("spawned") # for debuging

		self.Block_list.append(list(block_design[random_choice]))
	def rotate(self):
		current_block = self.Block_list[-1]

		color = current_block[-1]
		boolean = current_block[-2]

		current_block.pop(-1)
		current_block.pop(-1)

		# finding the pivit point
		middle_point = math.ceil(len(current_block)/2)

		px, py = current_block[middle_point][0], current_block[middle_point][1]

		rotated_block = []

		for i in current_block:
			x = i[1]+(px-py)
			y = px+(py-i[0])
			rotated_block.append([x, y])

		rotated_block.append(boolean)
		rotated_block.append(color)

		self.Block_list[-1] = list(rotated_block)
	
