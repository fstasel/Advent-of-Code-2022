from itertools import chain


f = open('input.txt', 'r')
data = f.read().splitlines()
pos = [(int(row[2][2:-1]), int(row[3][2:-1]), int(row[8][2:-1]),    # ugh
        int(row[9][2:])) for row in [line.split() for line in data]]
intervals = []
dest_y = 2000000
for sx, sy, bx, by in pos:           # create list of coverage intervals
    d = abs(sx - bx) + abs(sy - by)
    dy = abs(sy - dest_y)
    x1, x2 = sx - d + dy, sx + d - dy
    if x1 <= x2:
        intervals.append((x1, x2))
x1 = min([k for k, _ in intervals])
x2 = max([k for _, k in intervals])
print(x2-x1)

# part 2
search_range = chain.from_iterable((d, u) for d, u in zip(
    range(2000000, -1, -1), range(2000001, 4000001)))
for dest_y in search_range:  # exhaustive search from mid point
    intervals = []           # better algorithm?
    for sx, sy, bx, by in pos:
        d = abs(sx - bx) + abs(sy - by)
        dy = abs(sy - dest_y)
        x1, x2 = sx - d + dy, sx + d - dy
        if x1 <= x2:
            intervals.append((x1, x2))
    R = [(0, 4000000)]      # interval subtraction algorithm does well
    for lo, hi in intervals:
        Rnew = []
        for rlo, rhi in R:
            if rhi < lo or rlo > hi:
                Rnew.append((rlo, rhi))
            else:
                s1 = lo - 1
                s2 = hi + 1
                if rlo <= s1:
                    Rnew.append((rlo, s1))
                if s2 <= rhi:
                    Rnew.append((s2, rhi))
        R = Rnew
        if R == []:
            break
    if len(R) > 0:
        print(R)
        print(dest_y)
        print(R[0][0] * 4000000 + dest_y)
        break
