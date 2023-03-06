def move_head(dir, pos):
    if dir == "L": pos[0]-=1
    if dir == "R": pos[0]+=1
    if dir == "U": pos[1]+=1
    if dir == "D": pos[1]-=1
    return pos

def get_distance(Head, Tail):
    return (Head[0]-Tail[0])*(Head[0]-Tail[0])+(Head[1]-Tail[1])*(Head[1]-Tail[1])

file = open("input.txt", "r")
lines = file.read()
Head = [0,0]
Tail = [0,0]
TailTrail = []
for line in lines.split("\n")[0:-1]:
    for i in range(int(line.split(" ")[1])):
        if Tail not in TailTrail: TailTrail.append(Tail.copy())
        Head = move_head(line.split(" ")[0], Head)
        if (get_distance(Head, Tail) > 4):
            if (Head[0] < Tail[0]): Tail[0]-=1
            else: Tail[0]+=1
            if (Head[1] < Tail[1]): Tail[1]-=1
            else: Tail[1]+=1
        elif (get_distance(Head, Tail) > 2):
            Tail = move_head(line.split(" ")[0], Tail)

print ("result first  puzzle:", len(TailTrail))
print ("result second puzzle:", "not started")
