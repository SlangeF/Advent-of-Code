def heighest(line, max):
    best = -1
    index = -1
    for i in range(len(line)):
        value = line[i]
        if value > best:
            best = value
            index = i
        if (best >= max): return (best,index+1)
    return (best,len(line))

def visable(array, x, y):
    covered = 0

    wtrees = array[x][0:y][::-1]
    ntrees = [array[z][y] for z in range(x)][::-1]
    etrees = array[x][y+1:]
    strees = [array[z][y] for z in range(x+1,len(array))]

    if (heighest(wtrees, array[x][y])[0] >= array[x][y]): covered += 1;
    if (heighest(etrees, array[x][y])[0] >= array[x][y]): covered += 1;
    if (heighest(ntrees, array[x][y])[0] >= array[x][y]): covered += 1;
    if (heighest(strees, array[x][y])[0] >= array[x][y]): covered += 1;

    if covered == 4: return False
    return True

def view(array, x, y):
    wtrees = array[x][0:y][::-1]
    ntrees = [array[z][y] for z in range(x)][::-1]
    etrees = array[x][y+1:]
    strees = [array[z][y] for z in range(x+1,len(array))]

    west  = heighest(wtrees, array[x][y])[1]
    north = heighest(ntrees, array[x][y])[1]
    east  = heighest(etrees, array[x][y])[1]
    south = heighest(strees, array[x][y])[1]

    return west * north * east * south

file = open("input.txt", "r")
lines = file.read()
array = [[int(x) for x in line] for line in lines.split("\n")[0:-1]]

visible = 0
best = 0
for y in range(len(array)):
    for x in range(len(array[0])):
        visible += visable(array, x, y)
        scenic = view(array, x, y)
        if (scenic > best): best = scenic

print ("result first  puzzle:", visible)
print ("result second puzzle:", best)
