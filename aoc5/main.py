def readStack(lines, col):
    sbegin = 0
    send = 7
    s = []
    for i in range(send, sbegin-1, -1):
        t = lines[i][col]
        if t == ' ':
            break
        s.append(t)
    return s


def readAllStacks(lines):
    s = []
    for col in range(1, 34, 4):
        s.append(readStack(lines, col))
    return s


def move(stacks, f, t, n=0):
    if n == 0:
        return
    i = stacks[f].pop()
    stacks[t].append(i)
    move(stacks, f, t, n-1)


def move2(stacks, f, t, n=0):
    if n == 0:
        return
    i = stacks[f][-n:]
    del stacks[f][-n:]  # stacks[f] = stacks[f][:-n]
    stacks[t].extend(i)


f = open("input.txt", "r")
lines = f.read().splitlines()
stacks = readAllStacks(lines)

mbegin = 10

# print(stacks)

for i in range(mbegin, len(lines)):
    w = lines[i].split(' ')
    n = int(w[1])
    fr = int(w[3])-1
    to = int(w[5])-1
    # move(stacks,fr,to,n)
    move2(stacks, fr, to, n)

print(stacks)

for s in stacks:
    print(s[-1], end='')
print()
