class TreeNode:
    def __init__(self, parent, type, name, size, depth):
        self.parent = parent
        self.type = type
        self.name = name
        self.size = size
        self.depth = depth
        self.children = []

    def Print_Tree(self):
        for i in range(self.depth): print("  ", end='')
        if (self.type == "dir"):
            if self.size == -1:
                print("- ", self.name, " (dir)", sep = '')
            else:
                print("- ", self.name, " (dir, size:", self.size,")", sep = '')
            for child in self.children:
                child.Print_Tree()
        else:
            print("- ", self.name, " (file, size:", self.size,")", sep = '')

    def calculate_size(self):
        if (self.type == "file"): return
        self.size = 0
        for child in self.children:
            child.calculate_size()
            self.size += child.size

    def puzzle_1(self):
        if (self.type == "file"): return 0
        answer = 0;
        for child in self.children: answer += child.puzzle_1()
        if (self.size > 100000): return answer
        else: return answer + self.size

    def puzzle_2(self):
        if (self.type == "file"): return -1
        best = 70000000
        for child in self.children:
            temp = child.puzzle_2()
            if temp == -1: continue
            if temp < best: best = temp
        if (self.size < 30000000-(70000000 - root.size)): return best
        else:
            if (self.size < best): return self.size
            return best

file = open("input.txt", "r")
lines = file.read()
root = TreeNode(None, "dir", "/", -1, 0)
current = root
for line in lines.split("\n")[0:-1]:
    if (line[0] == '$'):
        if "$ cd" in line:
            goto = line.split(" ")[2]
            if goto == "..":
                current = current.parent
            elif goto == "/":
                while current.parent != None: current = current.parent
            else:
                for child in current.children:
                    if child.name == goto: current = child
    else:
        if (line[0:3] == "dir"):
            dn = line.split(" ")[1]
            current.children.append(TreeNode(current, "dir", dn, -1, current.depth+1))
        else:
            size, fn = line.split(" ")
            current.children.append(TreeNode(current, "file", fn, int(size), current.depth+1))
root.calculate_size()
#root.Print_Tree()

print ("result first  puzzle:", root.puzzle_1())
print ("result second puzzle:", root.puzzle_2())
