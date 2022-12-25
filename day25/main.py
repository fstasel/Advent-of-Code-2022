def toDec(s):
    d, p = 0, 1
    dig = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    for c in s[::-1]:
        d += p * dig[c]
        p *= 5
    return d


def toSNAFU(d):
    n = []
    while d > 0:
        n.append(d % 5)
        d //= 5
    for i in range(len(n)):
        if n[i] > 4:
            n[i] -= 5
            if i < len(n):
                n[i+1] += 1
            else:
                n.append(1)
        elif n[i] > 2:
            if i < len(n):
                n[i+1] += 1
            else:
                n.append(1)
    dig = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}
    return ''.join([dig[k] for k in n])[::-1]


nums = open('input.txt', 'r').read().splitlines()
s = sum([toDec(n) for n in nums])
snafu = toSNAFU(s)
print(snafu, s, toDec(snafu))
