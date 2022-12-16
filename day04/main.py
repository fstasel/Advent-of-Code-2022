f = open("input.txt", "r")
lines = f.read().splitlines()

d = [[[int(v) for v in s.split('-')] for s in row.split(',')] for row in lines]

c = 0
for p in d:
    if p[0][0] <= p[1][0] and p[0][1] >= p[1][1]    \
            or p[1][0] <= p[0][0] and p[1][1] >= p[0][1]:
        c += 1
print(c)

# part 2
c = 0
for p in d:
    if not (p[0][1] < p[1][0] or p[1][1] < p[0][0]):
        c += 1
print(c)
