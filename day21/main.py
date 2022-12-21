import operator as op
import re


def eval(m, val={}, expr={}):
    if m in val:
        return val[m]
    o, a, b = expr[m]
    # r = val[m] = o(eval(a, val, expr), eval(b, val, expr))
    r = o(eval(a, val, expr), eval(b, val, expr))
    return r


def check(n, a, b, val, expr):
    val['humn'] = n
    r1 = eval(a, val, expr)
    r2 = eval(b, val, expr)
    return (r1, r2)


data = open('input.txt', 'r').read().splitlines()
pat = re.compile(r"(\w+): (?:(\w+) ([-\+\*/]) (\w+)|(\d+))")
val = {}
expr = {}
oper = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
for line in data:
    m, a, o, b, l = re.findall(pat, line)[0]
    if o == '':
        val[m] = int(l)
    else:
        expr[m] = (oper[o], a, b)


# part 1
print(eval('root', val, expr))

# part 2
high = 100000000000000000
low = -100000000000000000
_, a, b = expr['root']
# check direction
r1h, r2h = check(high, a, b, val, expr)
r1l, r2l = check(low, a, b, val, expr)
up = True if r1h - r2h > r1l - r2l else False
while low <= high:
    mid = (high + low) // 2
    r1, r2 = check(mid, a, b, val, expr)
    print(mid, low, high, r1, r2)
    if r1 == r2:
        break
    if (up and r1 < r2) or (not up and r1 > r2):
        low = mid + 1
    else:
        high = mid - 1
print(mid)
