from functools import reduce


# autocorrelation func. for period detection
def acorr(x):
    c = [0] * len(x)
    xx = x + x
    for i in range(len(c)):
        c[i] = sum([xx[j + i] * x[j] for j in range(len(x))])
    return c


NCHECK = 100
NSAMPLE = 1000

# NROCKS = 2022
NROCKS = 1000000000000

jet = open('input.txt', 'r').read().strip()
ljet = len(jet)
r = [[(0, 0), (1, 0), (2, 0), (3, 0)],
     [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
     [(2, 0), (2, 1), (2, 2), (1, 2), (0, 2)],
     [(0, 0), (0, 1), (0, 2), (0, 3)],
     [(0, 0), (1, 0), (0, 1), (1, 1)]]
rh = [1, 3, 3, 4, 2]
c = [[True] * 9]
ch = [0] * 7    # for part 2
delh = 0        # for part 2
dellist = []    # for part 2
hr = 0
ji = 0
ri = 0
while ri < NROCKS:
    cur = r[ri % 5]
    curh = rh[ri % 5]
    if len(c) - hr < 4 + curh:
        c.extend([[True, False, False, False, False, False, False, False, True]
                 for _ in range(4 + curh - len(c) + hr)])

    x = 3
    y = hr + curh + 3

    while True:
        cuj = jet[ji % ljet]
        if cuj == '>':
            col = reduce(lambda a, b: a or b, [
                c[y - yy][x + xx + 1] for xx, yy in cur])
            if not col:
                x += 1
        else:
            col = reduce(lambda a, b: a or b, [
                c[y - yy][x + xx - 1] for xx, yy in cur])
            if not col:
                x -= 1
        ji += 1

        col = reduce(lambda a, b: a or b, [
            c[y - yy - 1][x + xx] for xx, yy in cur])
        if not col:
            y -= 1
        else:
            for xx, yy in cur:
                c[y - yy][x + xx] = True
                hr = max(hr, y - yy)
                # required for part 2
                if ch[x + xx - 1] < y - yy:
                    ch[x + xx - 1] = y - yy
                #####################
            # clean up mem (part 2)
            mch = min(ch)
            if (ri + 1) % NCHECK == 0:
                c = c[mch:]
                ch = [y - mch for y in ch]
                delh += mch
                hr -= mch
                dellist.append(mch)
                print(len(dellist), '/', NSAMPLE)
                if len(dellist) == NSAMPLE:
                    # samples collected
                    # cant wait till the end of the universe
                    # let's warp up
                    ac = acorr(dellist)
                    period = ac.index(max(ac[1:]))
                    if dellist[-period:] == dellist[-period-period:-period]:
                        print(period)
                    else:
                        print('failed')
                        exit(1)
                    todel = ((NROCKS - (ri + 1)) // (period * NCHECK)) \
                        * sum(dellist[-period:])
                    delh += todel
                    NROCKS = (NROCKS - (ri + 1)) % (period *
                                                    NCHECK) + (ri + 1) % 5
                    ri = (ri + 1) % 5 - 1
            break
    ri += 1

    # draw chamber for testing purposes
    # for i in range(len(c) - 1, -1, -1):
    #     for j in range(9):
    #         print('#' if c[i][j] else ' ', end='')
    #     print()

print(hr + delh)          # total height
