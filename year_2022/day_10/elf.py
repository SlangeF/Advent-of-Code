def complete_cycle(cycle, x, signal_strength, screen):
    if cycle in range(1,241,40): screen.append([])
    screen[(cycle-1)//40].append((cycle-1)%40 in range(x-1,x+2))
    if cycle in range(20,260,40): signal_strength[cycle] = cycle * x
    cycle += 1
    return cycle

def print_line(line):
    for pixel in line:
        if pixel: print("#", end='')
        else: print(".", end='')

def print_screen(screen):
    for line in screen:
        print_line(line)
        print()

file = open("input.txt", "r")
lines = file.read()
x = 1
cycle = 1
signal_strength = {}
screen = []
for line in lines.split("\n")[0:-1]:
    if (line == "noop"):
        cycle = complete_cycle(cycle, x, signal_strength, screen)
    else:
        for i in (0,1): cycle = complete_cycle(cycle, x, signal_strength, screen)
        x+= int(line.split(" ")[1])

result = 0
for key in signal_strength: result += signal_strength[key]

print ("result first  puzzle:", result)
print ("result second puzzle:")
print_screen(screen)
