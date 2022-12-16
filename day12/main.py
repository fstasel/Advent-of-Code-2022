import heapq as hq

f = open('input.txt', 'r')
lines = f.read().splitlines()

H = len(lines)
W = len(lines[0])

start = [(i, j) for i in range(H) for j in range(W) if lines[i][j] == 'S'][0]
end = [(i, j) for i in range(H) for j in range(W) if lines[i][j] == 'E'][0]
lines[start[0]] = lines[start[0]].replace('S', 'a')
lines[end[0]] = lines[end[0]].replace('E', 'z')


visit = [[False for _ in range(W)] for _ in range(H)]
id = 0
heap = []


def add(node, dest):
    global visit, id, heap
    if dest[0] < 0 or dest[0] >= H or dest[1] < 0 or dest[1] >= W:
        return
    if visit[dest[0]][dest[1]]:
        return
    if ord(lines[node[2][0]][node[2][1]]) - ord(lines[dest[0]][dest[1]]) < 2:
        id += 1
        visit[dest[0]][dest[1]] = True
        hq.heappush(heap, (node[0] + 1, id, dest))


visit[end[0]][end[1]] = True
hq.heappush(heap, (0, id, end))
while len(heap) > 0:
    node = hq.heappop(heap)
    if lines[node[2][0]][node[2][1]] == 'a':
        # The 1st line printed is the answer of part II
        print('To a' + str(node))
    if node[2] == start:
        # The last line printed is the answer of part I
        print('To S' + str(node))
        break
    i, j = node[2][0], node[2][1]
    add(node, (i+1, j))
    add(node, (i-1, j))
    add(node, (i, j+1))
    add(node, (i, j-1))
