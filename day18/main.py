lines = open('input.txt').read().splitlines()
cubes = set([[(int(x), int(y), int(z)) for x, y, z in [c.split(',')]][0]
             for c in lines])

surf = sum([sum(map(lambda v: 1 if v not in cubes else 0,
                    [(x+1, y, z), (x-1, y, z), (x, y+1, z),
                     (x, y-1, z), (x, y, z+1), (x, y, z-1)]))
            for x, y, z in cubes])
print(surf)

# part 2
xx = [x for x, _, _ in cubes]
yy = [y for _, y, _ in cubes]
zz = [z for _, _, z in cubes]

x1, x2, y1, y2, z1, z2 = min(xx)-1, max(xx) + 1, \
    min(yy)-1, max(yy)+1, min(zz)-1, max(zz)+1


def fill(water, seed):
    global cubes, x1, x2, y1, y2, z1, z2
    stack = [seed]
    while len(stack) > 0:
        seed = stack.pop()
        x, y, z = seed
        if (seed not in cubes) and (seed not in water) \
                and x >= x1 and x <= x2 and y >= y1 and y <= y2 and z >= z1 and z <= z2:
            water.add((x, y, z))
            stack.append((x+1, y, z))
            stack.append((x-1, y, z))
            stack.append((x, y+1, z))
            stack.append((x, y-1, z))
            stack.append((x, y, z+1))
            stack.append((x, y, z-1))


water = set()
fill(water, (x1, y1, z1))
surf = sum([sum(map(lambda v: 1 if v in water else 0,
                    [(x+1, y, z), (x-1, y, z), (x, y+1, z),
                     (x, y-1, z), (x, y, z+1), (x, y, z-1)]))
            for x, y, z in cubes])
print(surf)
