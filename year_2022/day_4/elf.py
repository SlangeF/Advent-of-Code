file = open("input.txt", "r")
lines = file.read()
sections = [[0,0],[0,0]]
total1 = 0
total2 = 0

for line in lines.split("\n")[0:-1]:
    sections[0][0] = int(line.split(",")[0].split("-")[0])
    sections[0][1] = int(line.split(",")[0].split("-")[1])
    sections[1][0] = int(line.split(",")[1].split("-")[0])
    sections[1][1] = int(line.split(",")[1].split("-")[1])

    if ((sections[0][0] >= sections[1][0] and sections[0][1] <= sections[1][1]) or
        (sections[1][0] >= sections[0][0] and sections[1][1] <= sections[0][1])):
        total1 += 1

	#puzzle 2
    if (sections[0][0] < sections[1][0]):
        if (sections[0][1] >= sections[1][0]):
            total2 += 1
    else:
        if (sections[1][1] >= sections[0][0]):
            total2 += 1

print("result first  puzzle:", total1)
print("result second puzzle:", total2)
