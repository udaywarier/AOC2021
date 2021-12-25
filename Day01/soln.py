depths = []
with open('./input.txt', 'r') as f:
    depths = f.readlines()

depths = [int(elem) for elem in depths]

count = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        count = count + 1

print('Depth measurements larger than the previous one: ' + str(count))

count_window = 0

for j in range(1, len(depths) - 2):
    common = depths[j] + depths[j + 1]
    lower_window_sum = common + depths[j - 1]
    upper_window_sum = common + depths[j + 2]
    if upper_window_sum > lower_window_sum:
        count_window = count_window + 1

print('Triple sliding window sums larger than the previous one: ' + str(count_window))