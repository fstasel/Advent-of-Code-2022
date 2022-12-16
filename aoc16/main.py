import heapq as hq
import itertools
import re


lines = open('input.txt', 'r').read().splitlines()
pat = re.compile(
    r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)+")
data = list(map(lambda s: pat.findall(s)[0], lines))
graph = {n: (int(f), list(e.split(', '))) for n, f, e in data}
move_cost = {}

for node in graph:
    nodecost = {}
    heap = []
    visit = set()
    hq.heappush(heap, (0, node))
    while len(heap) > 0:
        cost, name = hq.heappop(heap)
        if name not in nodecost:
            nodecost[name] = cost
        visit.add(name)
        for new in graph[name][1]:
            if new not in visit:
                hq.heappush(heap, (cost+1, new))
    move_cost[node] = nodecost


def deepen(route=[], tp=0, tf=0, rem=30, g={}):
    global move_cost, maxtp
    cur = route[-1]
    curflow = g[cur][0]
    if rem > 0 and curflow > 0:
        tp += tf
        tf += curflow
        rem -= 1
    for n in g:
        if n not in route and g[n][0] > 0 and rem >= move_cost[cur][n]:
            deepen(route + [n], tp + tf * move_cost[cur]
                   [n], tf, rem - move_cost[cur][n], g)
    tp += rem * tf
    if tp > maxtp:
        maxtp = tp


# part 1
maxtp = 0
deepen(['AA'], g=graph)
print(maxtp)

# part 2


def partition(predicate, iterable):
    it1, it2 = itertools.tee(iterable)
    return filter(predicate, it1), itertools.filterfalse(predicate, it2)


valves = {n: graph[n] for n in graph if graph[n][0] > 0}
maxtottp = 0
for p1, p2 in [[{x[1]:graph[x[1]] for x in p} for p in partition(lambda tuple: tuple[0],
                zip(mask, valves))] for mask in itertools.product([True, False], repeat=len(valves))]:
    # divide graph into two partitions w/ common start
    part1 = {'AA': graph['AA']}
    part1.update(p1)
    part2 = {'AA': graph['AA']}
    part2.update(p2)
    # re-run tests
    tottp = 0
    maxtp = 0
    deepen(['AA'], 0, 0, 26, part1)
    tottp += maxtp
    maxtp = 0
    deepen(['AA'], 0, 0, 26, part2)
    tottp += maxtp
    if tottp > maxtottp:
        maxtottp = tottp
print(maxtottp)
