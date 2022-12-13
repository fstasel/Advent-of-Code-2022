import ast
import functools


def check(a, b):
    if type(a) is int and type(b) is int:
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0
    if type(a) is int and type(b) is list:
        return check([a], b)
    if type(a) is list and type(b) is int:
        return check(a, [b])
    if len(a) == 0 and len(b) == 0:
        return 0
    if len(a) == 0 and len(b) > 0:
        return 1
    if len(a) > 0 and len(b) == 0:
        return -1
    c = check(a[0], b[0])
    if c == 1 or c == -1:
        return c
    return check(a[1:], b[1:])


f = open('input.txt', 'r')
rowpairs = f.read().split('\n\n')
pairs = [list(map(lambda x: ast.literal_eval(x), p.splitlines()))
         for p in rowpairs]
print(sum([i+1 for i in range(len(pairs)) if check(pairs[i][0], pairs[i][1]) == 1]))

# part 2
packets = sum(pairs, [])
packets.extend([[[2]], [[6]]])
packets.sort(key=functools.cmp_to_key(check), reverse=True)
print((packets.index([[2]])+1)*(packets.index([[6]])+1))
