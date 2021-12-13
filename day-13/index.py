chunks = [(i) for i in open('day-13/input.txt', 'r').read().split('\n\n')]

points = [[int(j) for j in i.split(',')] for i in chunks[0].split('\n')]
folds = [i.split(' ')[-1].split('=') for i in chunks[1].split('\n')]

max_x = 0
max_y = 0
for p in points:
    if p[0] + 1 > max_x:
        max_x = p[0] + 1
    if p[1] + 1 > max_y:
        max_y = p[1] + 1

paper = [[False] * max_x for i in range(max_y)]

for i in range(len(points)):
    point = points[i]
    paper[point[1]][point[0]] = True

for line in folds:
    dir = line[0]
    val = int(line[1])
    if dir == 'x':
        for i in range(len(paper[0]) - 1, val - 1, -1):
            for j in range(len(paper)):
                paper[j][val * 2 - i] = paper[j][val * 2 - i] or paper[j][i]
                paper[j].pop(i)
    else:
        for i in range(len(paper) - 1, val - 1, -1):
            for j in range(len(paper[0])):
                paper[val * 2 - i][j] = paper[val * 2 - i][j] or paper[i][j]
            paper.pop(i)

for i in paper:
    line = ''
    for j in i:
        line += '#' if j else '.'
    print(line)