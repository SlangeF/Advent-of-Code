file = open("input.txt", "r")
lines = file.read()
total = 0
total2 = 0

for line in lines.split("\n")[0:-1]:
    them = ord(line[0]) - ord('A') + 1
    me = ord(line[2]) - ord('X') + 1

    # puzzle 1
    if (me == them): total += 3
    elif (me == them%3+1): total += 6
    else: total += 0
    total += me

    # puzzle 2
    if (line[2] == 'Y'): total2 += 3 + them
    elif (line[2] == 'Z'): total2 += 6 + (them)%3 + 1
    else: total2 += 0 + (them + 1)%3 + 1

print("result first  puzzle:", total)
print("result second puzzle:", total2)
