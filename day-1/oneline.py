print(sum([1 if i > j else 0 for i, j in zip([int(i) for i in open('day-1/input.txt', 'r').read().split('\n')][3:], [int(i) for i in open('day-1/input.txt', 'r').read().split('\n')])]))