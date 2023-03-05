file = open("input.txt", "r")
lines = file.read()
temp = 0
best = 0
better = 0
good = 0

for line in lines.split("\n")[0:-1]:
    if line == '':
        if temp > best:
            good = better
            better = best
            best = temp
        elif temp > better:
            good = better
            better = temp
        elif temp > good:
            good = temp
        temp = 0
    else: temp += int(line)
    
print("result first  puzzle:", best)
print("result second puzzle:",best+better+good)
