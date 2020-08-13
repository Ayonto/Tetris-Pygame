import random
class Block:
	def __init__(self):
		self.Block_list = []
		# self.block_design = [[3, 1, True], [4, 1, True]]
		self.lastOneDone = False
		# self.color = (255, 255, 255)
	def spawn(self):
		random_choice = random.randint(0, 4)
		block_design = [[[3, 0], [3, 1], [4, 1], True, [255, 0, 0]], [[3, 0], [4, 0], [5, 0], True, [0, 255, 0]], [[3, 0], [3, 1], [4, 0], [4, 1], True, [0, 0, 255]],
						[[3, 0], [4, 0], [4, 1], [5, 1], True, [0, 255, 255]], [[3, 0], [3, 1], True, [255, 0, 255]]]
		# color_list = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [0, 255, 255], [255, 0, 255], [155, 155, 0]]
		# block_design = [[3, 0], [3, 1], [4, 1], True]
		print("spawned")
		self.Block_list.append(list(block_design[random_choice]))
		# self.color = color_list[random_choice]
		# self.Block_list.append(list(block_design))
	
