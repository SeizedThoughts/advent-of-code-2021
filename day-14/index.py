input = [(i) for i in open('day-14/input.txt', 'r').read().split('\n\n')]
polymer = input[0]
insertions = {}
for i in input[1].split('\n'):
    insertions[i.split(' -> ')[0]] = i.split(' -> ')[1]

buckets = {}

for i in range(len(polymer) - 1):
    part = polymer[i:i + 2]
    if not part in buckets:
        buckets[part] = 0
    buckets[part] += 1

counts = {}

for c in list(polymer):
    if not c in counts:
        counts[c] = 0
    counts[c] += 1

for _ in range(40):
    temp = {}
    for part in buckets:
        c = insertions[part]
        if not c in counts:
            counts[c] = 0
        counts[c] += buckets[part]
        if not part[0] + c in temp:
            temp[part[0] + c] = 0
        temp[part[0] + c] += buckets[part]
        if not c + part[1] in temp:
            temp[c + part[1]] = 0
        temp[c + part[1]] += buckets[part]
    buckets = temp

counts = sorted([counts[k] for k in counts])
print(counts[-1] - counts[0])