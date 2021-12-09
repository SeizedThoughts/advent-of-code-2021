input = [[int(j) for j in i] for i in open('day-9/input.txt', 'r').read().split('\n')]

def checkNeighbors(i, j, size = 0):
    ret = size
    height = input[i][j]
    if height == 9:
        return ret
    else:
        input[i][j] = 9
        ret += 1
        if i > 0:
            ret = checkNeighbors(i - 1, j, ret)
        if i < len(input) - 1:
            ret = checkNeighbors(i + 1, j, ret)
        if j > 0:
            ret = checkNeighbors(i, j - 1, ret)
        if j < len(input[i]) - 1:
            ret = checkNeighbors(i, j + 1, ret)
        return ret

regions = []

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 9:
            continue
        
        region = checkNeighbors(i, j)

        regions.append(region)

boop = sorted(regions)[-3:]

print(boop[0] * boop[1] * boop[2])