f = open("input.txt", "r")
lines = f.read().splitlines()

sums = []
s = 0
for e in lines:
    if e == "":
        sums.append(s)
        s = 0
    else:
        s += int(e)

sums.sort(reverse = True)
print(sums)
print(sums[0])
print(sum(sums[0:3]))