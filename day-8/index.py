input = [[j.split(' ') for j in (i).split(' | ')] for i in open('day-8/input.txt', 'r').read().split('\n')]

def getChar(schema, char):
    ret = -1
    for i in range(len(schema)):
        if len(diff(schema[i], char)) == 0 and len(diff(char, schema[i])) == 0:
            ret = i
            break
    return ret

def diff(str1, str2):
    temp = list(str1)
    for char in str2:
        if char in temp:
            temp.remove(char)

    ret = ''
    for i in temp:
        ret += i
    return ret
    

def getSchema(arr):
    schema = 10 * ['']
    schema[1] = arr[0]
    schema[7] = arr[1]
    schema[4] = arr[2]
    schema[8] = arr[9]

    fives = []
    sixes = []

    for i in arr:
        if len(i) == 6:
            sixes.append(i)
        elif len(i) == 5:
            fives.append(i)
    
    for i in sixes:
        if len(diff(i, schema[4])) == 2:
            schema[9] = i
            sixes.remove(i)
            break
    
    for i in sixes:
        if len(diff(i, schema[1])) == 4:
            schema[0] = i
            sixes.remove(i)
            schema[6] = sixes[0]
            break

    for i in fives:
        if len(diff(i, schema[1])) == 3:
            schema[3] = i
            fives.remove(i)
            break
    
    for i in fives:
        if len(diff(i, schema[4])) == 3:
            schema[2] = i
            fives.remove(i)
            schema[5] = fives[0]
            break
    
    return schema

summand = 0

for i in range(len(input)):
    schema = getSchema(sorted(input[i][0], key = len))
    out = input[i][1]
    number = 0
    base = 1
    for j in range(len(out) - 1, -1, -1):
        number += getChar(schema, out[j]) * base
        base *= 10
    summand += number

print(summand)