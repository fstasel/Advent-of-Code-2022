def check(maze, x, y, dir, width, height):
    global vec
    dx, dy = vec[dir]
    xx, yy = x, y
    c = w = d = 0
    f = False
    while True:
        xx = (xx + dx) % width
        yy = (yy + dy) % height
        if xx < len(maze[yy]):
            if maze[yy][xx] == '#':
                break
            if maze[yy][xx] == ' ':
                w += 1
            else:
                c += 1
                if w == 0:
                    d += 1
            if xx == x and yy == y:
                f = True
                break
        else:
            w += 1
    return (c, f, d, w)


data = open('input.txt', 'r').read()
puzzle = data.split('\n\n')
maze = puzzle[0].split('\n')
path = puzzle[1].strip()
walk = path.replace('L', ' ').replace('R', ' ')
turn = ''.join([p if w == ' ' else ' ' for p, w in zip(path, walk)]).split()
walk = [int(w) for w in walk.split()]
h = len(maze)
w = max(len(row) for row in maze)
vec = [(1, 0), (0, 1), (-1, 0), (0, -1)]
bound = {}
stx = sty = 0
for y, row in enumerate(maze):
    for x, col in enumerate(row):
        if col == '.':
            if stx == 0:
                stx, sty = x, y
            bound[(x, y)] = [check(maze, x, y, d, w, h) for d in range(4)]
sx, sy = stx, sty
d = 0
for i in range(len(walk)):
    # walk
    dx, dy = vec[d]
    m, f, dist, wrap = bound[(sx, sy)][d]
    if f:
        a = walk[i] % m
    else:
        a = min(walk[i], m)
    sx = (sx + (a + (wrap if a > dist else 0)) * dx + w) % w
    sy = (sy + (a + (wrap if a > dist else 0)) * dy + h) % h
    # turn
    if i < len(turn):
        d = (d + (1 if turn[i] == 'R' else -1) + 4) % 4

print((sy+1)*1000 + (sx+1)*4 + d)


# part 2
def ran(a, b, k=50):
    if a < b:
        r = list(range(a, b+1))
    else:
        r = list(range(a, b-1, -1))
    if len(r) == 1:
        r *= k
    return r


def ap(portal, s1, s2, sd, d1, d2, dd):
    s1x, s1y = s1
    s2x, s2y = s2
    d1x, d1y = d1
    d2x, d2y = d2
    for sx, sy, dx, dy in zip(ran(s1x, s2x), ran(s1y, s2y), ran(d1x, d2x), ran(d1y, d2y)):
        portal[(sx, sy, sd)] = (dx, dy, dd)


# this portal design has been specified for my input
portal = {}
ap(portal, (50, 0), (99, 0), 3, (0, 150), (0, 199), 0)
ap(portal, (100, 0), (149, 0), 3, (0, 199), (49, 199), 3)
ap(portal, (149, 0), (149, 49), 0, (99, 149), (99, 100), 2)
ap(portal, (100, 49), (149, 49), 1, (99, 50), (99, 99), 2)
ap(portal, (99, 50), (99, 99), 0, (100, 49), (149, 49), 3)
ap(portal, (99, 100), (99, 149), 0, (149, 49), (149, 0), 2)
ap(portal, (50, 149), (99, 149), 1, (49, 150), (49, 199), 2)
ap(portal, (49, 150), (49, 199), 0, (50, 149), (99, 149), 3)
ap(portal, (0, 199), (49, 199), 1, (100, 0), (149, 0), 1)
ap(portal, (0, 150), (0, 199), 2, (50, 0), (99, 0), 1)
ap(portal, (0, 100), (0, 149), 2, (50, 49), (50, 0), 0)
ap(portal, (0, 100), (49, 100), 3, (50, 50), (50, 99), 0)
ap(portal, (50, 50), (50, 99), 2, (0, 100), (49, 100), 1)
ap(portal, (50, 0), (50, 49), 2, (0, 149), (0, 100), 0)

sx, sy = stx, sty
d = 0
for i in range(len(walk)):
    # walk
    for _ in range(walk[i]):
        if (sx, sy, d) in portal:
            nx, ny, nd = portal[(sx, sy, d)]
        else:
            dx, dy = vec[d]
            nx, ny, nd = sx + dx, sy + dy, d
        if maze[ny][nx] == '#':
            break
        sx, sy, d = nx, ny, nd
    # turn
    if i < len(turn):
        d = (d + (1 if turn[i] == 'R' else -1) + 4) % 4

print((sy+1)*1000 + (sx+1)*4 + d)
