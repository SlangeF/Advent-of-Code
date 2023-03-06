def make_snake(size):
    snake = []
    for i in range(size): snake.append([0,0])
    return snake

def move_head(dir, pos):
    if dir == "L": pos[0]-=1
    if dir == "R": pos[0]+=1
    if dir == "U": pos[1]+=1
    if dir == "D": pos[1]-=1

def move_tail(snake, tailtrail):
    for i in range(1, len(snake)):
        if (get_distance(snake[i-1], snake[i]) > 4):
            if (snake[i-1][0] < snake[i][0]): snake[i][0]-=1
            else: snake[i][0]+=1
            if (snake[i-1][1] < snake[i][1]): snake[i][1]-=1
            else: snake[i][1]+=1
        elif (get_distance(snake[i-1], snake[i]) > 2):
            if   (snake[i-1][0] < snake[i][0]): snake[i][0]-=1
            elif (snake[i-1][0] > snake[i][0]): snake[i][0]+=1
            elif (snake[i-1][1] < snake[i][1]): snake[i][1]-=1
            else: snake[i][1]+=1
    if snake[-1] not in tailtrail: tailtrail.append(snake[-1].copy())

def get_distance(Head, Tail):
    return (Head[0]-Tail[0])*(Head[0]-Tail[0])+(Head[1]-Tail[1])*(Head[1]-Tail[1])

file = open("input.txt", "r")
lines = file.read()

Snake = make_snake(2)
Snake2 = make_snake(10)
TailTrail = []
TailTrail2 = []

for line in lines.split("\n")[0:-1]:
    for i in range(int(line.split(" ")[1])):
        move_head(line.split(" ")[0], Snake[0])
        move_tail(Snake, TailTrail)
        move_head(line.split(" ")[0], Snake2[0])
        move_tail(Snake2, TailTrail2)

print ("result first  puzzle:", len(TailTrail))
print ("result second puzzle:", len(TailTrail2))
