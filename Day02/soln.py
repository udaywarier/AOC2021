course = []
with open('./input.txt', 'r') as f:
    course = f.readlines()

course = [[elem.split(' ')[0], int(elem.split(' ')[1])]for elem in course]

horizontal_pos = 0
depth = 0

for direction,distance in course:
    if direction == 'forward':
        horizontal_pos += distance
    elif direction == 'up':
        depth -= distance
    else:
        depth += distance

print('Multiplying horizontal position by depth: ' + str(horizontal_pos * depth))

horizontal_pos = 0
depth = 0
aim = 0

for direction,distance in course:
    if direction == 'forward':
        horizontal_pos += distance
        depth += aim * distance
    elif direction == 'up':
        aim -= distance
    else:
        aim += distance

print('Multiplying horiztontal position by depth with aim: ' + str(horizontal_pos * depth))