def getPri(x=''):
    if x.islower():
        c = ord(x) - ord('a') + 1
    else:
        c = ord(x) - ord('A') + 27
    return c


def getCommon(c1, c2):
    box1 = [0] * 52
    box2 = [0] * 52
    for i in c1:
        box1[getPri(i)-1] += 1
    for i in c2:
        box2[getPri(i)-1] += 1
    c = [x > 0 and y > 0 for x, y in zip(box1, box2)]
    return c


f = open("input.txt", "r")
lines = f.read().splitlines()
# print(lines)

total = 0
for k in lines:
    c1 = k[:len(k)//2]
    c2 = k[len(k)//2:]
    c = getCommon(c1, c2)
    for i in range(52):
        if c[i]:
            total += i+1
print(total)

###########
# part 2


def getCommon3(c1, c2, c3):
    box1 = [0] * 52
    box2 = [0] * 52
    box3 = [0] * 52
    for i in c1:
        box1[getPri(i)-1] += 1
    for i in c2:
        box2[getPri(i)-1] += 1
    for i in c3:
        box3[getPri(i)-1] += 1
    c = [x > 0 and y > 0 and z > 0 for x, y, z in zip(box1, box2, box3)]
    return c


groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
# print(groups)
total2 = 0
for g in groups:
    c = getCommon3(g[0], g[1], g[2])
    for i in range(52):
        if c[i]:
            total2 += i+1
print(total2)
