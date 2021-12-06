input = open('day-4/input.txt', 'r').read().split('\n\n')

balls = input[0].split(',')
cards = [[j.split(' ') for j in i.split('\n')] for i in input[1:]]
cardData = [[[False for i in range(5)] for i in range(5)] for i in range(len(cards))]

for i in cards:
    for j in i:
        while '' in j:
            j.remove('')

def hasWon(cardDatum):
    won = False
    for row in cardDatum:
        if not False in row:
            won = True
            break
    
    if not won:
        for i in range(5):
            count = 0
            for row in cardDatum:
                if row[i]:
                    count += 1
            if count == 5:
                won = True
                break
    return won

def unmarked(cardDatum, card):
    sum = 0

    for i in range(5):
        for j in range(5):
            if not cardDatum[i][j]:
                sum += int(card[i][j])
    
    return sum

last = list(range(len(cards)))
winner = False
index = -1
lastBall = -1

for i in range(len(balls)):
    ball = int(balls[i])
    for j in range(len(cards)):
        for k in range(5):
            for l in range(5):
                square = int(cards[j][k][l])
                if ball == square:
                    cardData[j][k][l] = True
    
    for j in range(len(cards)):
        index = j
        lastBall = ball
        if hasWon(cardData[j]) and j in last:
            last.remove(j)

        if len(last) == 0:
            break
    if len(last) == 0:
        break

print(lastBall * unmarked(cardData[index], cards[index]))