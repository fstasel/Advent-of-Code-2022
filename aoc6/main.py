f = open("input.txt", "r")
data = f.read()

# part1
for i in range(len(data)-3):
    p = data[i:i+4]
    if p[0] != p[1] and p[0] != p[2] and p[0] != p[3] and p[1] != p[2] and p[1] != p[3] and p[2] != p[3]:
        print(i+4)
        break

# part2
for i in range(len(data)-13):
    p = [ord(k)-ord('a') for k in data[i:i+14]]
    box = [False] * 26
    flag = False
    for j in p:
        if box[j]:
            flag = True
            break
        box[j] = True
    if not flag:
        print(i+14)
        break
