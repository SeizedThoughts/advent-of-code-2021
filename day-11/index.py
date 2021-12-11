input = [[int(j) for j in (i) ]for i in open('day-11/input.txt', 'r').read().split('\n')]

def flash(points):
    nextPoints = []
    for point in points:
        if input[point[0]][point[1]] > 9:
            if point[0] > 0 and input[point[0] - 1][point[1]] < 10:
                input[point[0] - 1][point[1]] += 1
                if input[point[0] - 1][point[1]] > 9:
                    nextPoints.append((point[0] - 1, point[1]))
            if point[0] < len(input) - 1 and input[point[0] + 1][point[1]] < 10:
                input[point[0] + 1][point[1]] += 1
                if input[point[0] + 1][point[1]] > 9:
                    nextPoints.append((point[0] + 1, point[1]))
            if point[1] > 0 and input[point[0]][point[1] - 1] < 10:
                input[point[0]][point[1] - 1] += 1
                if input[point[0]][point[1] - 1] > 9:
                    nextPoints.append((point[0], point[1] - 1))
            if point[1] < len(input[0]) - 1 and input[point[0]][point[1] + 1] < 10:
                input[point[0]][point[1] + 1] += 1
                if input[point[0]][point[1] + 1] > 9:
                    nextPoints.append((point[0], point[1] + 1))
            if point[0] > 0 and point[1] > 0 and input[point[0] - 1][point[1] - 1] < 10:
                input[point[0] - 1][point[1] - 1] += 1
                if input[point[0] - 1][point[1] - 1] > 9:
                    nextPoints.append((point[0] - 1, point[1] - 1))
            if point[0] < len(input) - 1 and point[1] > 0 and input[point[0] + 1][point[1] - 1] < 10:
                input[point[0] + 1][point[1] - 1] += 1
                if input[point[0] + 1][point[1] - 1] > 9:
                    nextPoints.append((point[0] + 1, point[1] - 1))
            if point[0] > 0 and point[1] < len(input[0]) - 1 and input[point[0] - 1][point[1] + 1] < 10:
                input[point[0] - 1][point[1] + 1] += 1
                if input[point[0] - 1][point[1] + 1] > 9:
                    nextPoints.append((point[0] - 1, point[1] + 1))
            if point[0] < len(input) - 1 and point[1] < len(input[0]) - 1 and input[point[0] + 1][point[1] + 1] < 10:
                input[point[0] + 1][point[1] + 1] += 1
                if input[point[0] + 1][point[1] + 1] > 9:
                    nextPoints.append((point[0] + 1, point[1] + 1))

    if len(nextPoints) > 0:
        flash(nextPoints)

step = 0
ended = False
while(not ended):
    flashpoints = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            input[i][j] += 1
            if input[i][j] > 9:
                flashpoints.append((i, j))
    flash(flashpoints)
    all = True
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] > 9:
                input[i][j] = 0
            if all and not input[i][j] == 0:
                all = False
    ended = all
    step += 1

print(step)