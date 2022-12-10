class Entry:
    def __init__(self) -> None:
        self.isDir = False
        self.name = ''
        self.size = 0
        self.contains = []
        self.parent = None

    def __init__(self, isDir, name, size, contains, parent) -> None:
        self.isDir = isDir
        self.name = name
        self.size = size
        self.contains = contains
        self.parent = parent

    def append(self, e):
        self.contains.append(e)
        e.parent = self

    def find(self, name):
        for c in self.contains:
            if c.name == name:
                return c
        return None

    def print(self):
        print(self.name + ' ' + str(self.isDir) + ' ' + str(self.size))
        for c in self.contains:
            c.print()

    def getSize(self):
        return self.size + sum([c.getSize() for c in self.contains])

    def getDirs(self, recursive=False):
        dirs = [d for d in self.contains if d.isDir]
        if recursive:
            for d in self.contains:
                if d.isDir:
                    dirs.extend(d.getDirs(True))
        return dirs


f = open("input.txt", "r")
lines = f.read().splitlines()

root = Entry(isDir=True, name='/', size=0, contains=[], parent=None)
current = root

for line in lines:
    words = line.split(' ')
    if words[0] == '$':
        if words[1] == 'cd':
            if words[2] == '/':
                current = root
            elif words[2] == '..':
                current = current.parent
            else:
                current = current.find(words[2])
    elif words[0] == 'dir':
        current.append(
            Entry(isDir=True, name=words[1], size=0, contains=[], parent=current))
    else:
        s = int(words[0])
        current.append(
            Entry(isDir=False, name=words[1], size=s, contains=[], parent=current))


root.print()

# part 1
total = sum([d.getSize() for d in root.getDirs(True) if d.getSize() <= 100000])
print(total)

# part 2
free = 70000000 - root.getSize()
need = 30000000 - free
sizes = [d.getSize() for d in root.getDirs(True) if d.getSize() >= need]
sizes.sort()
print(sizes[0])
