input = sorted([int(i) for i in open('day-7/input.txt', 'r').read().split(',')])

lowest = -1
total_dist = [0 for i in range(input[-1])]

for i in range(input[-1]):
    for j in input:
        total_dist[i] += int((abs(i - j) + 1) * abs(i - j) / 2)
    if lowest > total_dist[i] or lowest == -1:
        lowest = total_dist[i]
    

print(lowest)