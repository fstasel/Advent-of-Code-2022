import heapq as hq


def addstate(mi, cx, cy, bl):
    global heap, visit, data, ex, ey, wt, ht
    if cx < 0 or cy < 0 or cx >= wt or cy >= ht:
        return
    if data[cy][cx] == '#':
        return
    d = abs(cx-ex) + abs(cy-ey)
    if (cx, cy, 0, -1) not in bl and (cx, cy, 0, 1) not in bl and \
            (cx, cy, -1, 0) not in bl and (cx, cy, 1, 0) not in bl and \
            (cx, cy, mi) not in visit:
        hq.heappush(heap, (mi, d, cx, cy, bl))
        visit.add((cx, cy, mi))


data = open('input.txt', 'r').read().splitlines()
sx, sy = data[0].index('.'), 0
ex, ey = data[-1].index('.'), len(data)-1
wt, ht = len(data[0]), len(data)
left, right, top, bottom = 1, wt-2, 1, ht-2
bliz = []
for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c == '^':
            bliz.append((x, y, 0, -1))
        elif c == 'v':
            bliz.append((x, y, 0, 1))
        elif c == '<':
            bliz.append((x, y, -1, 0))
        elif c == '>':
            bliz.append((x, y, 1, 0))
bliz = frozenset(bliz)
d = abs(sx-ex) + abs(sy-ey)
istate = (0, d, sx, sy, bliz)
heap = [istate]
visit = set()
visit.add((sx, sy, 0))
iter = 0
phase = 0
while len(heap) > 0:
    mi, d, cx, cy, bl = hq.heappop(heap)

    if iter % 1000 == 0:
        print(iter, ':', 'heap:', len(heap), 'visit:',
              len(visit), 'min:', mi, 'dist:', d)
    iter += 1

    if cx == ex and cy == ey:
        print(mi)
        if phase < 2:
            sx, sy, ex, ey = ex, ey, sx, sy
            d = abs(sx-ex) + abs(sy-ey)
            istate = (mi, d, sx, sy, bl)
            heap = [istate]
            visit = set()
            visit.add((sx, sy, mi))
            iter = 0
            phase += 1
            continue
        else:
            break
    bliz = []
    for bx, by, dx, dy in bl:
        bx, by = bx+dx, by+dy
        bx = right if bx < left else bx
        bx = left if bx > right else bx
        by = bottom if by < top else by
        by = top if by > bottom else by
        bliz.append((bx, by, dx, dy))
    bliz = frozenset(bliz)
    addstate(mi+1, cx, cy, bliz)  # wait
    addstate(mi+1, cx, cy+1, bliz)  # down
    addstate(mi+1, cx, cy-1, bliz)  # up
    addstate(mi+1, cx+1, cy, bliz)  # right
    addstate(mi+1, cx-1, cy, bliz)  # left
