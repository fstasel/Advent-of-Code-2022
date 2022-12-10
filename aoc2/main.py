f = open("input.txt", "r")
lines = f.read().splitlines()

s = 0
for li in lines:
    p1 = ord(li[0]) - ord('A') + 1
    p2 = ord(li[2]) - ord('X') + 1
    if p1 == p2:
        s += p2 + 3
    elif p1 == 3 and p2 == 1 or p1 < p2 and not (p1 == 1 and p2 == 3):
        s += p2 + 6
    else:
        s += p2
print(s)

s = 0
for li in lines:
    p1 = ord(li[0]) - ord('A') + 1
    p2 = ord(li[2]) - ord('X') + 1
    if p2 == 2:
        s += p1 + 3
    elif p2 == 3:
        k = p1 + 1
        if k == 4:
            k = 1
        s += k + 6
    else:
        k = p1 - 1
        if k == 0:
            k = 3
        s += k
print(s)
