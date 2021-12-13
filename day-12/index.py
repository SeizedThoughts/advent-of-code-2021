input = [(i).split('-') for i in open('day-12/input.txt', 'r').read().split('\n')]

cave = {}

for i in range(len(input)):
    line = input[i]
    if not line[0] in cave:
        cave[line[0]] = []
    if not line[1] in cave:
        cave[line[1]] = []
    cave[line[0]].append(line[1])
    cave[line[1]].append(line[0])

paths = []

def createAllPaths(past_moves):
    options = cave[past_moves[-1]]
    for option in options:
        if not option == 'start' and ((past_moves.count(option) < 2 and not '___' in past_moves) or ('___' in past_moves and not option in past_moves) or option.isupper()):
            if option == 'end':
                if past_moves[0] == '___':
                    past_moves.pop(0)
                paths.append(','.join(past_moves))
                paths[-1] += ','
                paths[-1] += option
            else:
                moves = past_moves.copy()
                if option in past_moves and option.islower():
                    moves.append('___')
                moves.append(option)
                createAllPaths(moves)
createAllPaths(['start'])

paths = list(set(paths))

print(len(paths))