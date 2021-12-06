input = [i.split(" ") for i in open('day-2/input.txt', 'r').read().split('\n')]

position = [0, 0, 0]

for i in range(len(input)):
    line = input[i]
    if line[0] == "forward":
        position[0] += int(line[1])
        position[1] += (int(line[1]) * position[2])
    elif line[0] == "up":
        position[2] -= int(line[1])
    elif line[0] == "down":
        position[2] += int(line[1])

print(position[0] * position[1])