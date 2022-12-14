f = open('input.txt', 'r')
data = f.read().splitlines()
coords = [[[int(c) for c in line.split(',')]
           for line in rawline.split(' -> ')] for rawline in data]
sandsrc = [500, 0]
xlist = [c[0] for c in sum(coords, [])] + [sandsrc[0]]
ylist = [c[1] for c in sum(coords, [])] + [sandsrc[1]]
xmin = min(xlist)
xmax = max(xlist)
ymin = min(ylist)
ymax = max(ylist)
W = xmax - xmin + 1
H = ymax - ymin + 1
world = set()
sand = set()


def printImage(world, sand):
    global xmin, ymin, W, H
    image = [['.' for _ in range(W)] for _ in range(H)]
    for (x, y) in world:
        image[y - ymin][x - xmin] = '#'
    for (x, y) in sand:
        image[y - ymin][x - xmin] = 'o'
    for r in image:
        for c in r:
            print(c, end='')
        print()


def sign(a):
    return 1 if a > 0 else -1 if a < 0 else 0


def drawLine(world, line):
    for i in range(len(line)-1):
        if line[i][0] == line[i+1][0]:
            for y in range(line[i][1], line[i+1][1], sign(line[i+1][1] - line[i][1])):
                world.add((line[i][0], y))
            world.add((line[i][0], line[i+1][1]))
        else:
            for x in range(line[i][0], line[i+1][0], sign(line[i+1][0] - line[i][0])):
                world.add((x, line[i][1]))
            world.add((line[i+1][0], line[i][1]))


def createWorld(world, coords):
    for line in coords:
        drawLine(world, line)


def addSand(world, sand):
    global sandsrc, ymax
    pos = (sandsrc[0], sandsrc[1])
    flag = 0
    while flag == 0:
        if pos[1] == ymax:
            return -1
        if (pos[0], pos[1]+1) not in world and (pos[0], pos[1]+1) not in sand:
            pos = (pos[0], pos[1]+1)
        elif (pos[0]-1, pos[1]+1) not in world and (pos[0]-1, pos[1]+1) not in sand:
            pos = (pos[0]-1, pos[1]+1)
        elif (pos[0]+1, pos[1]+1) not in world and (pos[0]+1, pos[1]+1) not in sand:
            pos = (pos[0]+1, pos[1]+1)
        else:
            if pos in sand:
                return 2    # part 2 condition
            sand.add(pos)
            flag = 1
    return 1


createWorld(world, coords)
count = 0
while addSand(world, sand) == 1:
    count += 1
printImage(world, sand)
print(count)

# part 2
ymax += 2
xmin = min(xmin, sandsrc[0] - (ymax - sandsrc[1]))
xmax = max(xmax, sandsrc[0] + (ymax - sandsrc[1]))
W = xmax - xmin + 1
H = ymax - ymin + 1
coords.append([[xmin, ymax], [xmax, ymax]])
world = set()
sand = set()
createWorld(world, coords)
count = 0
while addSand(world, sand) == 1:
    count += 1
printImage(world, sand)
print(count)
