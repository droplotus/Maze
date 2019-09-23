from tkinter import *
import math
import random
import time

# initialization canvas
root = Tk()
canvas = Canvas(root, width=1000, height=1000, bg="#333333")
canvas.pack()

# some global variables
w = 10;
cols = math.floor(int(canvas["width"])/w)
rows = math.floor(int(canvas["height"])/w)
grid = []
current = None

class Cell():
	line_color = "#AAAAAA"
	visited_color = "green"
	visited = False
	rectangle = None

	def __init__(self, i, j):
		self.i = i
		self.j = j
		self.wall = [True, True, True, True] # top , right, bottom, left

	def __repr__(self):
		return "({}, {})".format(self.i, self.j)

	def draw_lines(self):
		x = self.i*w
		y = self.j*w
		
		if self.visited :
			self.rectangle = canvas.create_rectangle(x, y, x+w, y+w, fill="purple", outline="")
			canvas.update()

		if self.wall[0]:
			self.top = canvas.create_line(x, y, x+w, y, fill=self.line_color)
		else:
			self.top = canvas.create_line(x, y, x+w, y, fill="purple")
		if self.wall[1]:
			self.right = canvas.create_line(x+w, y, x+w, y+w, fill=self.line_color)
		else:
			self.right = canvas.create_line(x+w, y, x+w, y+w, fill="purple")
		if self.wall[2]:
			self.bottom = canvas.create_line(x, y+w, x+w, y+w, fill=self.line_color)
		else:
			self.bottom = canvas.create_line(x, y+w, x+w, y+w, fill="purple")
		if self.wall[3]:
			self.left = canvas.create_line(x, y, x, y+w, fill=self.line_color)
		else:
			self.left = canvas.create_line(x, y, x, y+w, fill="purple")

	def checkNeighbors(self):
		neighbors = []
		top = None
		bottom = None
		left = None
		right = None
		if index(self.i, self.j-1) != -1:
			top = grid[index(self.i, self.j-1)]

		if index(self.i, self.j+1) != -1:
			bottom = grid[index(self.i, self.j+1)]

		if index(self.i-1, self.j) != -1:
			left = grid[index(self.i-1, self.j)]

		if index(self.i+1, self.j) != -1:
			right = grid[index(self.i+1, self.j)]

		if top is not None and top.visited is False:
			neighbors.append(top)
		if right is not None and right.visited is False:
			neighbors.append(right)
		if bottom is not None and bottom.visited is False:
			neighbors.append(bottom)
		if left is not None and left.visited is False:
			neighbors.append(left)

		if len(neighbors) > 0:
			r = random.randint(0, len(neighbors)-1)
			return neighbors[r]
		else:
			return None

def removeWalls(a, b):
	x = a.i - b.i
	y = a.j - b.j
	
	if x != 0:
		if x == 1:
			a.wall[3] = False
			b.wall[1] = False
		else:
			a.wall[1] = False
			b.wall[3] = False

	if y != 0:
		if y == 1:
			a.wall[0] = False
			b.wall[2] = False
		else:
			a.wall[2] = False
			b.wall[0] = False

def index(i, j):
	if j < 0 or j > rows - 1 or i < 0 or i > cols - 1:
		return -1
	return j + i * cols

def setup():
	global current
	for i in range(rows):
		for j in range(cols):
			cell = Cell(i, j)
			grid.append(cell)
	current = grid[0]



next_one = None
def draw():
	global current
	global next_one
	stack = []
	almost = False
	for cell in grid:
		cell.draw_lines()
	while True:
		current.visited = True
		next_one = current.checkNeighbors()
		
		if next_one:
			stack.append(current)
			removeWalls(current, next_one)
			current.draw_lines()
			next_one.draw_lines()
			current = next_one
		elif len(stack) > 0:
			cell = stack.pop()
			current = cell
		elif len(stack) == 0:
			for i in range(len(grid)):
				grid[i].draw_lines()
			break

for cell in grid:
	print(cell.visited)

setup()
draw()


root.mainloop()