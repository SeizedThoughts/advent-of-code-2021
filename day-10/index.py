input = [(i) for i in open('day-10/input.txt', 'r').read().split('\n')]

corrupted  = []

close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

closers = [')', ']', '}', '>']

openpoints = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

points = []

for i in range(len(input)):
    line = input[i]
    valid = True
    openings = []
    
    for char in line:
        if char in list(close):
            openings.append(char)
        elif char == close[openings[-1]]:
            openings.pop(-1)
        else:
            valid = False
            break

    sub = 0

    if valid:
        for j in range(len(openings) - 1, -1, -1):
            sub *= 5
            sub += openpoints[openings[j]]
        points.append(sub)

print(sorted(points)[int(len(points) / 2)])