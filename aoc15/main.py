from itertools import chain


f = open('input.txt', 'r')
data = f.read().splitlines()
pos = [(int(row[2][2:-1]), int(row[3][2:-1]), int(row[8][2:-1]),
        int(row[9][2:])) for row in [line.split() for line in data]]
intervals = []
dest_y = 2000000
for p in pos:           # create list of coverage intervals
    d = abs(p[0] - p[2]) + abs(p[1] - p[3])
    dy = abs(p[1] - dest_y)
    x1, x2 = p[0] - d + dy, p[0] + d - dy
    if x1 <= x2:
        intervals.append((x1, x2))
x1 = min([k[0] for k in intervals])
x2 = max([k[1] for k in intervals])
print(x2-x1)

# part 2
search_range = chain.from_iterable((k[0], k[1]) for k in zip(
    list(range(2000000, -1, -1)), list(range(2000001, 4000001))))
for dest_y in search_range:  # exhaustive search from mid point
    intervals = []           # better algorithm?
    for p in pos:
        d = abs(p[0] - p[2]) + abs(p[1] - p[3])
        dy = abs(p[1] - dest_y)
        x1, x2 = p[0] - d + dy, p[0] + d - dy
        if x1 <= x2:
            intervals.append((x1, x2))
    R = [(0, 4000000)]      # interval subtraction algorithm does well
    for k in intervals:
        Rnew = []
        for r in R:
            if r[1] < k[0] or r[0] > k[1]:
                Rnew.append((r[0], r[1]))
            else:
                s1 = k[0] - 1
                s2 = k[1] + 1
                if r[0] <= s1:
                    Rnew.append((r[0], s1))
                if s2 <= r[1]:
                    Rnew.append((s2, r[1]))
        R = Rnew
    if (len(R) > 0):
        print(R)
        print(dest_y)
        print(R[0][0] * 4000000 + dest_y)
        break
