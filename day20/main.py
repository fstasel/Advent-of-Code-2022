class LList:
    def __init__(self, x) -> None:
        self.x = x
        self.next = self
        self.prev = self

    def insertAfter(self, node) -> None:
        node.next = self.next
        node.prev = self
        self.next = node
        node.next.prev = node

    def shiftRight(self) -> None:
        nnode = self.next
        pnode = self.prev
        self.next = nnode.next
        nnode.next.prev = self
        self.prev = nnode
        nnode.next = self
        nnode.prev = pnode
        pnode.next = nnode

    def shiftLeft(self) -> None:
        nnode = self.next
        pnode = self.prev
        self.prev = pnode.prev
        pnode.prev.next = self
        self.next = pnode
        pnode.prev = self
        pnode.next = nnode
        nnode.prev = pnode

    def __str__(self) -> str:
        out = ''
        cur = self
        while True:
            out += str(cur.x) + ' '
            cur = cur.next
            if cur is self:
                return out


data = open('input.txt', 'r').read().split()
num = [int(x) for x in data]
ptr = []
size = len(num)

head = None
cur = None
for i in num:
    if head is None:
        head = LList(i)
        cur = head
    else:
        cur.insertAfter(LList(i))
        cur = cur.next
    ptr.append(cur)

# part 1
# for node in ptr:
#     for _ in range(abs(node.x)):
#         if node.x > 0:
#             node.shiftRight()
#         else:
#             node.shiftLeft()
#########

# part 2
factor = 811589153
for node in ptr:
    node.x *= factor
for i in range(10):
    print('round', i)
    for node in ptr:
        for _ in range(abs(node.x) % (size-1)):
            if node.x > 0:
                node.shiftRight()
            else:
                node.shiftLeft()
#########

while head.x != 0:
    head = head.next
n1000 = head
for _ in range(1000):
    n1000 = n1000.next
n2000 = n1000
for _ in range(1000):
    n2000 = n2000.next
n3000 = n2000
for _ in range(1000):
    n3000 = n3000.next
print(n1000.x+n2000.x+n3000.x)
