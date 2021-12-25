import math

# Return the dominant bit at a given index for a given list, using a tiebreak if given.
def get_dominant_bit(idx, list, tiebreak=None):
	count_zeroes = 0
	count_ones = 0
	for elem in list:
		if int(elem[idx]) == 1:
			count_ones += 1
		else:
			count_zeroes += 1
	
	dominant_bit = -1

	if tiebreak and tiebreak == 1:
		dominant_bit = 1 if count_ones >= count_zeroes else 0
	else:
		dominant_bit = 1 if count_ones > count_zeroes else 0
	
	return dominant_bit

# Takes a number and flips all its bits from 0 -> 1 and 1 -> 0. Pads the number with leading zeros up to len if necessary.
def binary_inversion(num, len):
	return int(''.join(['1' if char == '0' else '0' for char in bin(num)[2:].zfill(len)]), 2)

# Read the contents of the input into a list
input = []
with open('./input.txt', 'r') as f:
	input = f.readlines()

# Get rid of the newline character
binary = [elem[0:len(elem) - 1] for elem in input]

# Length of each binary string.
binary_string_length = len(binary[0])

# Keep track of the number of ones in each digits place.
dominant_bits = [int(0)] * binary_string_length
for i in range(binary_string_length):
	dominant_bits[i] = get_dominant_bit(i, binary)

# Obtain the values of gamma and epsilon.
gamma = int(''.join([str(elem) for elem in dominant_bits]), 2)
epsilon = binary_inversion(gamma, binary_string_length)

print(gamma, epsilon)

# Calculate the power consumption rate and print.
power_consumption_rate = gamma * epsilon
print('Power consumption rate: ' + str(power_consumption_rate))

# Calculate most common string.
most_common_copy = [elem for elem in binary]
idx = 0
while len(most_common_copy) > 1:
	dominant_bit = str(get_dominant_bit(idx, most_common_copy, tiebreak=1))
	most_common_copy = [elem for elem in most_common_copy if elem[idx] == dominant_bit]
	idx = idx + 1

# Calculate least common string.
least_common_copy = [elem for elem in binary]
idx = 0
while len(least_common_copy) > 1:
	dominant_bit = str(1 - get_dominant_bit(idx, least_common_copy, tiebreak=1))
	least_common_copy = [elem for elem in least_common_copy if elem[idx] == dominant_bit]
	idx = idx + 1

# Obtain the two values.
oxygen_generator_rating = int(most_common_copy[0], 2)
CO2_scrubber_rating = int(least_common_copy[0], 2)

# Calculate the life support rating and print.
life_support_rating = oxygen_generator_rating * CO2_scrubber_rating
print('Life support rating: ' + str(life_support_rating))
