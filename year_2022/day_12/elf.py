class node:
    def __init__(self, x, y, depth, visited):
        visited.append([x,y])
        self.x = x
        self.y = y
        self.next = []
        self.depth = depth

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def get_loc(self):
        return (self.x,self.y)

    def get_leafs(self, depth):
        if self.next == [] and self.depth == depth:
            return [self]
        else:
            result = []
            for child in self.next:
                result += child.get_leafs(depth)
        return result

    def go_deeper(self, map, visited):
        for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
            pos_x = self.x + dir[0]
            pos_y = self.y + dir[1]
            if (pos_x < 0 or pos_y < 0 or pos_x >= len(map) or
                pos_y >= len(map[0]) or [pos_x,pos_y] in visited or
                map[pos_x][pos_y] < map[self.x][self.y]-1):
                continue
            self.next.append(node(pos_x,pos_y, self.depth+1, visited))

file = open("input.txt", "r")
lines = file.read()
map = []
visited = []
for line in lines.split("\n")[0:-1]:
    map.append([])
    for c in line:
        if c == 'S':
            end = (len(map)-1, len(map[-1]))
            map[-1].append(ord('a')-ord('a'))
        elif c == 'E':
            start = (len(map)-1, len(map[-1]))
            begin = node(len(map)-1, len(map[-1]), 0, visited)
            map[-1].append(ord('z')-ord('a'))
        else: map[-1].append(ord(c)-ord('a'))

i = 0
depth = -1
depth2 = -1
while depth < 0:
    for leaf in begin.get_leafs(i):
        if leaf.x == end[0] and leaf.y == end[1]: depth = leaf.depth
        if depth2 < 0 and map[leaf.x][leaf.y] == 0: depth2 = leaf.depth
        leaf.go_deeper(map, visited)
    i+=1

print ("result first  puzzle:", depth)
print ("result second puzzle:", depth2)
