import os

# Get all the folders labeled ./Day01, ./Day02, etc.
numbers_used = sorted([int(f.path[5:7]) for f in os.scandir('./') if f.is_dir() and f.path[2:5] == 'Day'])

# If the last Day is Day n, the next day will be Day n+1.
next_folder_number = numbers_used[len(numbers_used) - 1] + 1

# Get the name of the next folder by formatting the number properly.
next_folder_name = './Day' + '{:02d}'.format(next_folder_number)

# Create the next subdirectory.
os.system('mkdir ' + next_folder_name)

# Set the name of the starter file and its contents.
starter_file_name = next_folder_name + '/soln.py'
starter_file_contents = '# Read the contents of the input into a list\ninput = []\nwith open(\'./input.txt\', \'r\') as f:\n\tinput = [line.strip() for line in f.readlines()]'

# Create the starter file and write the given contents.
with open(starter_file_name, 'w') as fd:
    fd.write(starter_file_contents)

# Create a blank .txt file for the problem input.
input_file_name = next_folder_name + '/input.txt'
input_file_content = ''
with open(input_file_name, 'w') as ifd:
    ifd.write(input_file_content)