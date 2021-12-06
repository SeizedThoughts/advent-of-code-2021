input = open('day-3/input.txt', 'r').read().split('\n')

def base2to10(b2):
    out = 0
    place = 1
    b2 = b2[::-1]
    for i in range(len(input[0])):
        out += place * int(b2[i])
        place *= 2
    b2 = b2[::-1]
    return out


counts = [[0, 0] for i in input[0]]

for i in range(len(input)):
    line = input[i]
    for c in range(len(line)):
        counts[c][int(line[c])] += 1

gamma = ''
epsilon = ''

for i in counts:
    if i[0] < i[1]:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

possibleO2 = list(range(len(input)))

for i in range(len(input[0])):
    counts = [0, 0]
    for j in possibleO2:
        counts[int(input[j][i])] += 1

    test = '1'
    if counts[0] > counts[1]:
        test = '0'

    for j in range(len(input)):
        if not input[j][i] == test:
            if j in possibleO2:
                possibleO2.remove(j)
                
    if len(possibleO2) == 1:
        break

possibleCO2 = list(range(len(input)))

for i in range(len(input[0])):
    counts = [0, 0]
    for j in possibleCO2:
        counts[int(input[j][i])] += 1

    test = '0'
    if counts[0] > counts[1]:
        test = '1'

    for j in range(len(input)):
        if not input[j][i] == test:
            if j in possibleCO2:
                possibleCO2.remove(j)
                
    if len(possibleCO2) == 1:
        break

print(base2to10(input[possibleO2[0]]) * base2to10(input[possibleCO2[0]]))

gamma10 = base2to10(gamma)
epsilon10 = base2to10(epsilon)

print(gamma10 * epsilon10)