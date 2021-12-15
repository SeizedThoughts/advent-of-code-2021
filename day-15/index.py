new_text = ''

text = open('day-15/input.txt', 'r').read().split('\n')

part_size = len(text)

for i in range(5):
    for y in range(part_size):
        for x in range(part_size):
            new_text += str((int(text[y][x]) + i - 1) % 9 + 1)
        new_text += '\n'

text = new_text.split('\n')[:-1]

for i in range(4):
    for y in range(len(text)):
        for x in range(part_size):
            text[y] += str((int(text[y][x]) + i) % 9 + 1)

cave = [[[int(j), int(j)] for j in i] for i in text]

for y in range(len(cave) - 1, -1, -1):
    for x in range(len(cave[0]) - 1, -1, -1):
        if x + 1 < len(cave[0]) and y + 1 < len(cave):
            right = cave[y][x + 1][0]
            down = cave[y + 1][x][0]
            cave[y][x][0] += min(down, right)
        elif x + 1 < len(cave[0]):
            cave[y][x][0] += cave[y][x + 1][0]
        elif y + 1 < len(cave):
            cave[y][x][0] += cave[y + 1][x][0]

change = True
while(change):
    change = False
    for y in range(len(cave) - 1, -1, -1):
        for x in range(len(cave[0]) - 1, -1, -1):
            values = [cave[y][x][0]]
            if x - 1 > 0:
                values.append(cave[y][x - 1][0])
            if y - 1 > 0:
                values.append(cave[y - 1][x][0])
            if x + 1 < len(cave[0]):
                values.append(cave[y][x + 1][0])
            if y + 1 < len(cave):
                values.append(cave[y + 1][x][0])

            new = min(values)

            if cave[y][x][1] + new < values[0]:
                cave[y][x][0] = cave[y][x][1] + new
                change = True

print(min(cave[0][1][0], cave[1][0][0]))