points = [[[int(k) for k in j.split(',')] for j in i.split(' -> ')] for i in open('day-5/input.txt', 'r').read().split('\n')]

Y_MAX = 0
X_MAX = 0

for i in points:
    if i[0][0] + 1 > Y_MAX:
        Y_MAX = i[0][0] + 1
    if i[1][0] + 1 > Y_MAX:
        Y_MAX = i[1][0] + 1
    if i[0][1] + 1 > X_MAX:
        X_MAX = i[0][1] + 1
    if i[1][1] + 1 > X_MAX:
        X_MAX = i[1][1] + 1

grid = [[0 for x in range(X_MAX)] for y in range(Y_MAX)]

for i in range(len(points)):
    line = points[i]
    x1 = line[0][1]
    y1 = line[0][0]
    x2 = line[1][1]
    y2 = line[1][0]
    x_inc = 0
    y_inc = 0
    
    if x1 < x2:
        x_inc = 1
    elif x1 > x2:
        x_inc = -1
    
    if y1 < y2:
        y_inc = 1
    elif y1 > y2:
        y_inc = -1
    
    point_count = 0
    
    if x1 - x2 > point_count:
        point_count = x1 - x2
    if x2 - x1 > point_count:
        point_count = x2 - x1
    if y1 - y2 > point_count:
        point_count = y1 - y2
    if y2 - y1 > point_count:
        point_count = y2 - y1

    for p in range(point_count + 1):
        grid[y1 + (p * y_inc)][x1 + (p * x_inc)] += 1

crosses = 0

for y in grid:
    for x in y:
        if x > 1:
            crosses += 1

print(crosses)