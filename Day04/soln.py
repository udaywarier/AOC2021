class BingoBoard:

	# This is what we'll mark our boards with if the number matches.
	HIT_MARK = -69

	# Initialize a BingoBoard object with a 5x5 array of numbers.  
	def __init__(self, board):
		self.board = board

	# Make sure the bingo board is valid, i.e it contains 25 different numbers.
	def validate(self):
		flattened = [elem for lst in self.board for elem in lst]
		return len(set(flattened)) == 25
	
	# Process a bingo number, mark a cell as -69 if it matches.
	def process_number(self, num):
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if self.board[i][j] == num:
					self.board[i][j] = self.HIT_MARK
	
	# Check if we have bingo!
	def check_bingo(self):
		lines_to_check = []

		# Get all the rows in the board.
		for elem in self.board:
			lines_to_check.append(elem)
		
		# Get all the columns in the board.
		for i in range(5):
			lines_to_check.append([row[i] for row in self.board])
		
		# If one row/column matches, we have bingo! 
		for elem in lines_to_check:
			if elem == [self.HIT_MARK, self.HIT_MARK, self.HIT_MARK, self.HIT_MARK, self.HIT_MARK]:
				return True
		
		# If not, we don't.
		return False
	
	# Calculate the score of a winning board: total unmarked sum * last number called.
	def calculate_winning_score(self, last_num):
		unmarked_sum = 0
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if self.board[i][j] != self.HIT_MARK:
					unmarked_sum += self.board[i][j]
		
		return unmarked_sum * last_num
	
	# To string will just print the board.
	def __str__(self):
		str_rep = ''
		for row in self.board:
			for elem in row:
				str_rep += str(elem) + '\t'
			str_rep += '\n'

		return str_rep


# Read the contents of the input into a list
input = []
with open('./input.txt', 'r') as f:
	input = f.readlines()

# Strip the newlines from the input.
input = [elem[0:len(elem) - 1] for elem in input if elem != '\n']

# Extract the bingo numbers in order.
bingo_numbers = [int(elem) for elem in input[0].split(',')]
input.pop(0)

# Extract all the bingo boards.
bingo_boards = []
curr_board = []
for elem in input:

	# Format the current row of the board as a list of integers.
	curr_board.append([int(num) for num in elem.split(' ') if num != ' ' and num != ''])

	# Add the bingo board to the list of bingo boards.
	if len(curr_board) == 5:
		bingo_obj = BingoBoard(curr_board)
		bingo_boards.append(bingo_obj)
		curr_board = []

# Keep track of the first and last boards to end.
first_board_iteration = 101
first_board = None
first_board_last_number = 0
last_board_iteration = -1
last_board = None
last_board_last_number = 0

# Now play bingo!
for i,board in enumerate(bingo_boards):
	for j,num in enumerate(bingo_numbers):

		# Process each bingo number.
		board.process_number(num)

		# If we have bingo, check whether this board is the first or last one to finish, and update the necessary variables.
		if board.check_bingo():
			if j < first_board_iteration:
				first_board_iteration = j
				first_board = board
				first_board_last_number = num
			if j > last_board_iteration:
				last_board_iteration = j
				last_board = board
				last_board_last_number = num
			break

# Calculate first and last winning scores and print.
first_board_winning_score = first_board.calculate_winning_score(first_board_last_number)
last_board_winning_score = last_board.calculate_winning_score(last_board_last_number)
print('First bingo board to finish has winning score: ' + str(first_board_winning_score))
print('Last bingo board to finish has winning score: ' + str(last_board_winning_score))
