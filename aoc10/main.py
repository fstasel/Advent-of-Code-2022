def cycles(instr):
    if instr == 'noop':
        return [0]
    return [0, int(instr.split(' ')[1])]


f = open('input.txt', 'r')
lines = f.read().splitlines()

c = sum(map(cycles, lines), [])
cc = [1]
for k in c:
    cc.append(k+cc[-1])
print(sum([cc[i-1] * i for i in [20, 60, 100, 140, 180, 220]]))

# part 2
for i in range(6):
    for j in range(40):
        if cc[j+i*40] - 1 <= j and cc[j+i*40] + 1 >= j:
            print('#', end='')
        else:
            print('.', end='')
    print()
