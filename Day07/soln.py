# Read the contents of the input into a list
input = []
with open('./input.txt', 'r') as f:
	input = [line.strip() for line in f.readlines()]