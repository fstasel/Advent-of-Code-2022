f = open("input.txt", "r")
lines = f.read().splitlines()

nrow = len(lines)
ncol = len(lines[0])
nvis = 0

for i in range(nrow):
    for j in range(ncol):
        ri = [lines[i][k] for k in range(j+1, ncol)
              if lines[i][k] >= lines[i][j]]
        le = [lines[i][k] for k in range(j-1, -1, -1)
              if lines[i][k] >= lines[i][j]]
        do = [lines[k][j] for k in range(i+1, nrow)
              if lines[k][j] >= lines[i][j]]
        up = [lines[k][j] for k in range(i-1, -1, -1)
              if lines[k][j] >= lines[i][j]]
        if len(ri) > 0 and len(le) > 0 and len(do) > 0 and len(up) > 0:
            nvis += 1

notvis = nrow * ncol - nvis
print(notvis)

# part 2
sc = []
for i in range(nrow):
    for j in range(ncol):
        ri = 0
        for k in range(j+1, ncol):
            ri += 1
            if lines[i][k] >= lines[i][j]:
                break
        le = 0
        for k in range(j-1, -1, -1):
            le += 1
            if lines[i][k] >= lines[i][j]:
                break
        do = 0
        for k in range(i+1, nrow):
            do += 1
            if lines[k][j] >= lines[i][j]:
                break
        up = 0
        for k in range(i-1, -1, -1):
            up += 1
            if lines[k][j] >= lines[i][j]:
                break
        sc.append(le*ri*up*do)
print(max(sc))
