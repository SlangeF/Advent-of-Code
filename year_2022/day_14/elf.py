def is_empty(rocks, sand, spot):
    if not spot in rocks and not spot in sand: return True
    return False

file = open("input.txt", "r")
lines = file.read()
lowest = 0
rocks = []
sand = []

for line in lines.split("\n")[0:-1]:
    last = 0
    for spot in line.split(" -> "):
        current = int(spot.split(",")[0]) * 1000 + int(spot.split(",")[1])
        if current%1000 > lowest: lowest = current%1000
        if not last == 0:
            if current//1000 == last//1000:
                while last%1000 != current%1000:
                    if last%1000 < current%1000: last = last + 1
                    else: last = last - 1
                    if last not in rocks: rocks.append(last)
            else:
                while last//1000 != current//1000:
                    if last//1000 < current//1000: last += 1000
                    else: last -= 1000
                    if last not in rocks: rocks.append(last)
        else:
            if current not in rocks: rocks.append(current)
            last = current
found = 0
while True:
    current = 500000
    while True:
        if current%1000 > lowest:
            if found == 0: found = len(sand)
            sand.append(current)
            break;
        elif is_empty(rocks, sand, current + 1): current += 1
        elif is_empty(rocks, sand, current - 999): current -= 999
        elif is_empty(rocks, sand, current + 1001): current += 1001
        else:
            sand.append(current)
            break;
    if (current == 500000): break;

print ("result first  puzzle:", found)
print ("result second puzzle:", len(sand))
