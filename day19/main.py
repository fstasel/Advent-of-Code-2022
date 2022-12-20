import re

lines = open('input.txt', 'r').read().splitlines()
pat = re.compile(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.")
costs = []
for b in lines:
    id, oror, clor, obor, obcl, geor, geob = map(int, re.findall(pat, b)[0])
    # 0     1       2       3
    # (ore, clay, obsidian, geode)
    costs.append(((oror, 0, 0, 0), (clor, 0, 0, 0),
                 (obor, obcl, 0, 0), (geor, 0, geob, 0)))
initr = [1, 0, 0, 0]    # 1 ore robot
initinv = [0, 0, 0, 0]  # empty inv


def able(inv, req):
    for i, r in zip(inv, req):
        if i < r:
            return False
    return True


# pack values in 4-bits wide so that large values produce collision
# resulting in reduction of search space
def pack(r, inv, rem):
    return r[0] | r[1] << 4 | r[2] << 8 | r[3] << 12 | \
        inv[0] << 16 | inv[1] << 20 | inv[2] << 24 | inv[3] << 28 | \
        rem << 32


def deepen(r, inv, rem=24):
    global costs, b, iter, best, visit
    g = inv[3]
    if rem == 0:
        if best[1] <= g:
            best = (iter, g, r, inv, rem)
        if iter % 100000 == 0:
            print('>', iter, best)
        iter += 1
        return g
    if pack(r, inv, rem) in visit:
        return g
    visit.add(pack(r, inv, rem))
    suf = [able(inv, costs[b][k]) for k in range(4)]
    if rem == 1:
        trials = [-1]
    elif suf[3]:
        trials = [3]
    else:
        trials = []
        if r[0] < costs[b][1][0] or r[0] < costs[b][2][0] or r[0] < costs[b][3][0]:
            trials += [0]
        if r[1] < costs[b][2][1]:
            trials += [1]
        if r[2] < costs[b][3][2]:
            trials += [2]
        trials += [-1]
    for k in trials:
        if k == -1:
            g = max(
                g, deepen(r, [a+b for a, b in zip(r, inv)], rem-1))
        elif suf[k]:
            g = max(g, deepen([r[i] + (1 if i == k else 0) for i in range(4)],
                    [a+b-c for a, b, c in zip(r, inv, costs[b][k])], rem-1))
    return g


# part 1
# res = 0
# for b in range(len(lines)):
#     visit = set()
#     iter = 0
#     best = (0, 0, [], [], 0)
#     g = deepen(initr, initinv)
#     print(b, g, best)
#     res += g * (b+1)
# print(res)


# part 2
res = 1
for b in range(3):
    visit = set()
    iter = 0
    best = (0, 0, [], [], 0)
    g = deepen(initr, initinv, 32)
    print(b, g, best)
    res *= g
print(res)
