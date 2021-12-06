fish = [int(i) for i in open('day-6/input.txt', 'r').read().split(',')]

meta = [0 for i in range(9)]

for i in fish:
    meta[i] += 1

def doDay(arr):
    arr.append(arr[0])
    arr.pop(0)
    arr[6] += arr[8]

for i in range(256):
    doDay(meta)

summand = 0

for i in meta:
    summand += i

print(summand)