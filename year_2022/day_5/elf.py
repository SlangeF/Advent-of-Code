def print_stacks(stacks):
    output = ""
    for stack in stacks: output += stack[-1]
    return output

def create_stacks(temp):
    stacks = []
    for value in temp[-1].split(" "):
        if value != "": stacks.append([])
    for line in reversed(temp[0:-1]):
        for i in range(1, len(line), 4):
            if (line[i] != ' '): stacks[int((i-1)/4)].append(line[i])
    return stacks

def copy_stacks(stacks):
    copy = []
    for stack in stacks: copy.append(stack.copy())
    return copy

file = open("input.txt", "r")
lines = file.read()
temp = []
stacks = []
stacks2 = []
for line in lines.split("\n")[0:-1]:
    if (len(line) == 0 or line[0] != 'm'):
        if (line != ""): temp.append(line)
        else:
            stacks = create_stacks(temp)
            stacks2 = copy_stacks(stacks)
    else:
        amount = int(line.split(" ")[1])
        fr = int(line.split(" ")[3]) -1
        to = int(line.split(" ")[5]) -1
        pos = len(stacks2[fr])-amount

        for i in range(amount):
            stacks[to].append(stacks[fr].pop()) # puzzle 1
            stacks2[to].append(stacks2[fr].pop(pos)) # puzzle 2

print ("result first  puzzle:", print_stacks(stacks))
print ("result second puzzle:", print_stacks(stacks2))
