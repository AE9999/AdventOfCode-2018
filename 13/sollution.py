import sys

rows = list(map(lambda x: list(x.rstrip()),  sys.stdin.readlines()))

carts = []

def replaceCart(x, y):
    global rows
    up = None if  y < 1 else rows[y-1][x]
    down = None if (y + 1) == len(rows) else rows[y+1][x]
    left = None if (x < 1) else rows[y][x]
    right = None if (x+1) == len(rows[y]) else rows[y][x+1]
    if False:
        return '|'
    if False:
        return '-'
    if False:
        return '/'
    if False:
        return '\\'
    if False:
        return '+'
    pass
pass

def handleDirection(direction, turn):
    t = turn % 3
    if direction == '>':
        if t == 0: return '^', (0, -1)
        if t == 1: return '>', (1, 0)
        if t == 2: return 'v', (0, 1)
    if direction == '<':
        if t == 0: return 'v', (0, 1)
        if t == 1: return '<', (-1, 0)
        if t == 2: return '^', (0, 1)
    if direction == 'v':
        if t == 0: return '>', (1, 0)
        if t == 1: return 'v', (0, 1)
        if t == 2: return '<', (-1, 0)
    if direction == '^':
        if t == 0: return '<', (-1, 0)
        if t == 1: return '^', (-1, 0)
        if t == 2: return '>', (1, 0)
pass


def nextStateCarte(cart):
    global rows
    direction, x, y, turns = cart[0], cart[1][0], cart[1][1], cart[2]
    cc = rows[cart[1][1]][cart[1][0]]
    if cc == '-':
        if direction == '<':
            return (direction, (x-1, y), turns)
        if direction == '>':
            return (direction, (x+1, y), turns)
        pass
    if cc == '/':
        if direction == '<':
            return ('v', (x, y - 1), turns)
        if direction == '^':
            return ('>', (x+1, y), turns)
        pass
    if cc == '+':
        ndirection, delta = handleDirection(direction, turns)
        return (ndirection,(x + delta[0], y + delta[1]) ,turns +1)
    if cc == '\\':
        if direction == '>':
            return ('v', (x, y - 1), turns)
        if direction == '^':
            return ('<', (x+1, y), turns)
        pass
    if cc == '|':
        if direction == '^':
            return (direction, (x, y - 1), turns)
        if direction == 'v':
            return (direction, (x, y + 1), turns)
        pass
    pass
pass

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] in "^<>v":
            carts.append((rows[y][x], (x,y), 0)) # direction, position turnstaken
            rows[y][x] = replaceCart(x, y)
        pass
    pass
pass

turn = 0
while True:
    carts = [ nextState(cart) for cart in carts ]
    turn += 1
pass