input = [int(i) for i in open('day-1/input.txt', 'r').read().split('\n')]

count = 0

for i in range(3, len(input)):
    this = input[i] + input[i-1] + input[i-2]
    last = input[i-1] + input[i-2] + input[i-3]
    if(this > last):
        count+=1

print(count)