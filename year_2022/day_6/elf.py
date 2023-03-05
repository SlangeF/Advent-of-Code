def check_marker (string, size):
    collection = []
    for i in range (size-1, len(string)):
        for j in range(size):
            if (string[i-j] not in collection):
                collection.append(string[i-j])
            else:
                collection = []
                break
        else: return i + 1

file = open("input.txt", "r")
lines = file.read()
line = lines.split("\n")[0]

print ("result first  puzzle:", check_marker(line, 4))
print ("result second puzzle:", check_marker(line, 14))
