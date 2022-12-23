from functools import reduce


lines = open('input.txt', 'r').read().splitlines()
elves = set()
for i, row in enumerate(lines):
    for j, c in enumerate(row):
        if c == '#':
            elves.add((i, j))
vec8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
        (0, 1), (1, -1), (1, 0), (1, 1)]
vec4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
vec43 = [[(-1, -1), (-1, 0), (-1, 1)], [(1, -1), (1, 0), (1, 1)],
         [(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)]]
round = 0
while True:
    trymove = {e for e in elves if reduce(
        lambda a, b: a or b, [(e[0]+i, e[1]+j) in elves for i, j in vec8])}
    if len(trymove) == 0:
        break
    prop = {}
    for ei, ej in trymove:
        dd = -1
        for d in [(round + n) % 4 for n in range(4)]:
            if reduce(lambda a, b: a and b, [
                    (ei+i, ej+j) not in elves for i, j in vec43[d]]):
                dd = d
                break
        if dd != -1:
            p = (ei + vec4[d][0], ej + vec4[d][1])
            if p in prop:
                prop[p] |= set([(ei, ej)])
            else:
                prop[p] = set([(ei, ej)])
    for p in prop:
        if len(prop[p]) == 1:
            e = list(prop[p])[0]
            elves.remove(e)
            elves.add(p)
    round += 1
    # if round == 10:      # commented out for part 2
    #     break

rows = [ei for ei, _ in elves]
cols = [ej for _, ej in elves]
h = max(rows) - min(rows) + 1
w = max(cols) - min(cols) + 1
empty = (h * w) - len(elves)
print(empty)
print(round+1)
