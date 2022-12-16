f = open('input.txt', 'r')
lines = f.read().splitlines()

head = (0, 0)
tail = (0, 0)

visit = set()
visit.add(tail)

for line in lines:
    m = line.split(' ')
    for i in range(int(m[1])):
        if m[0] == 'R':
            h = (head[0]+1, head[1])
        elif m[0] == 'L':
            h = (head[0]-1, head[1])
        elif m[0] == 'U':
            h = (head[0], head[1]-1)
        else:  # D
            h = (head[0], head[1]+1)
        x = abs(h[0] - tail[0])
        y = abs(h[1] - tail[1])
        if x > 1 or y > 1:
            tail = head
        head = h
        visit.add(tail)

print(len(visit))

# part 2

rope = [(0, 0)] * 10

visit = set()
visit.add(rope[9])

for line in lines:
    m = line.split(' ')
    for i in range(int(m[1])):
        if m[0] == 'R':
            h = (rope[0][0]+1, rope[0][1])
        elif m[0] == 'L':
            h = (rope[0][0]-1, rope[0][1])
        elif m[0] == 'U':
            h = (rope[0][0], rope[0][1]-1)
        else:  # D
            h = (rope[0][0], rope[0][1]+1)
        rope[0] = h

        for t in range(1, 10):
            x = abs(rope[t][0] - rope[t-1][0])
            y = abs(rope[t][1] - rope[t-1][1])
            if x > 1 or y > 1:
                if x < y:
                    rope[t] = (rope[t-1][0], (rope[t][1] + rope[t-1][1])//2)
                elif x > y:
                    rope[t] = ((rope[t][0] + rope[t-1][0])//2, rope[t-1][1])
                else:
                    rope[t] = ((rope[t][0] + rope[t-1][0])//2,
                               (rope[t][1] + rope[t-1][1])//2)
        # print(rope)
        visit.add(rope[9])

print(len(visit))
