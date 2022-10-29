import math

# Small, basic class to represent a point.
class Point:
	
	# Initialize a point as an (x,y) pair.
	def __init__(self, row, col):
		self.row = int(row)
		self.col = int(col)
	
	# True if two points form a horizontal line. 
	def is_horizontal(self, p2):
		return self.row == p2.row
		
	# True if two points form a vertical line.
	def is_vertical(self, p2):
		return self.col == p2.col

	# True if two points are diagonal.
	def is_diagonal(self, p2):
		return abs(self.row - p2.row) == abs(self.col - p2.col)
	
	# For colinear self and p2, returns in increasing order of variable dimension. 
	def sort(self, p2):
		if (self.row == p2.row and self.col < p2.col) or (self.col == p2.col and self.row < p2.row):
			return [self, p2]
		else:
			return [p2, self]
	
	# For diagonal points, sort by whichever has col < the other.
	def sort_diagonal(self, p2):
		if self.col < p2.col:
			return [self, p2]
		else:
			return [p2, self]
	
	# String representation of a point.
	def __str__(self):
		return '{row=' + str(self.row) + ',col=' + str(self.col) + '}'

# Class to represent a bunch of lines (which are just a bunch of Points) on a grid.
class Grid:

	# Hardcoded, but I scanned the input and noticed no points had a 4-digit coordinate.
	GRID_LENGTH = 1000
	GRID_WIDTH = 1000
	pass

	# Initialize an empty 1000x1000 grid.
	def __init__(self):
		self.grid = []
		for i in range(self.GRID_LENGTH):
			empty_row = [int(0)] * self.GRID_WIDTH
			self.grid.append(empty_row)
	
	# Draws a line from start -> end point. This will increment the value at each point on the line by 1.
	def add_line(self, point_start, point_end):
		curr_row = point_start.row
		curr_col = point_start.col
		diff_row = point_end.row - point_start.row
		diff_col = point_end.col - point_start.col
		row_step = -1 if (diff_row < 0) else (1 if diff_row > 0 else 0)
		col_step = -1 if (diff_col < 0) else (1 if diff_col > 0 else 0) 
		while True:
			self.add_point(Point(curr_row, curr_col))
			if curr_row == point_end.row and curr_col == point_end.col:
				break
			curr_row = curr_row + row_step
			curr_col = curr_col + col_step
	
	# Place a point on the grid.
	def add_point(self, point):
		self.grid[point.row][point.col] = self.grid[point.row][point.col] + 1
	
	# Get count of points in grid that are greater than the overlapping line threshold.
	def get_threshold_breach_count(self, threshold):
		ct = 0
		for i in range(self.GRID_LENGTH):
			for j in range(self.GRID_WIDTH):
				if self.grid[i][j] >= threshold:
					ct += 1
		return ct
	
	# Print a region of the grid, useful for debugging.
	def print_region(self, row_idx_start, row_idx_end, col_idx_start, col_idx_end):
		ret = ''
		for i in range(row_idx_start, row_idx_end):
			for j in range(col_idx_start, col_idx_end):
				ret += str(self.grid[i][j]) + '\t'
			ret += '\n'
		
		return ret
	
	# To string not super useful, but just print the grid.
	def __str__(self):
		return self.print_region(0, self.GRID_LENGTH, 0, self.GRID_WIDTH)

# Read the contents of the input into a list
input = []
with open('./input.txt', 'r') as f:
	input = [line.strip() for line in f.readlines()]

# Initialize an empty Grid.
grid = Grid()

# For each horizontal/vertical line segment, draw that line on the Grid.
for vent in input:
	points = vent.split(' -> ')
	left_point = Point(points[0].split(',')[1], points[0].split(',')[0])
	right_point = Point(points[1].split(',')[1], points[1].split(',')[0])
	if left_point.is_horizontal(right_point) or left_point.is_vertical(right_point):
		points_sorted = left_point.sort(right_point)
		grid.add_line(points_sorted[0], points_sorted[1])
	elif left_point.is_diagonal(right_point):
		points_sorted = left_point.sort_diagonal(right_point)
		grid.add_line(points_sorted[0], points_sorted[1])


OVERLAPPING_LINE_THRESHOLD = 2
print('Number of points where at least ' + str(OVERLAPPING_LINE_THRESHOLD) + ' lines overlap: ' + str(grid.get_threshold_breach_count(OVERLAPPING_LINE_THRESHOLD)))