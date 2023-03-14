def get_elements(line):
    elements = []
    level = 0
    current = ""
    for c in line:
        if c == '[': level += 1
        if c == ']': level -= 1
        if (level == 0 and c == ","):
            elements.append(current)
            current = ""
        else: current += c
    if current != '': elements.append(current)
    return elements

def is_list(test):
    if len(get_elements(test)) == 1 and test[0] == '[' and test[-1] == ']': return True
    else: return False

def compare(first, second):
    if (is_list(first) or is_list(second)):
        if (not is_list(first)): first = '[' + first + ']'
        if ( not is_list(second)): second = '[' + second + ']'
        left = get_elements(first[1:-1])
        right = get_elements(second[1:-1])
        for value in left:
            if len(right) == 0: return -1
            result = compare(value, right[0])
            del right[0]
            if result == 1 or result == -1: return result
        if len(right) > 0: return 1
        else: return 0
    else:
        if int(first) < int(second): return 1
        if int(first) > int(second): return -1
        if int(first) == int(second): return 0

def sort(list):
    unfinished = False
    for i in range(len(list[0:-1])):
        if compare(list[i],list[i+1]) != 1:
            list[i], list[i+1] = list[i+1], list[i]
            unfinished = True
    return unfinished

file = open("input.txt", "r")
lines = file.read()

first = ""
second = ""
index = 1
result_1 = 0
list = ["[[2]]","[[6]]"]

for line in lines.split("\n"):
    if first == "": first = line
    elif second == "": second = line
    else:
        if (compare(first,second) == 1): result_1 += index
        list.append(first)
        list.append(second)
        first = ""
        second = ""
        index += 1

unfinished = True
while (unfinished): unfinished = sort(list)

print ("result first  puzzle:", result_1)
print ("result second puzzle:", (list.index("[[2]]")+1)*(list.index("[[6]]")+1))
