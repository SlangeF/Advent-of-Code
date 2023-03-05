def get_value(let):
    if (ord(let) >= ord('a') and ord(let) <= ord('z')):
        return ord(let) - ord('a') + 1
    else:
        return ord(let) - ord('A') + 27

def get_character(first, second):
    for character in first:
        for char in second:
            if char == character:
                return char

def get_char(first, second, third):
    for character in first:
        for char in second:
            if char == character:
                for c in third:
                    if char == c:
                        return c

file = open("input.txt", "r")
lines = file.read()
total = 0
total2 = 0
set = []

for line in lines.split("\n")[0:-1]:
    # puzzle 1
    character = get_character(line[0:int(len(line)/2)],line[int(len(line)/2):])
    total += get_value(character)

    # puzzle 2
    set.append(line)
    if (len(set) == 3):
        character = get_char(set[0], set[1], set[2])
        total2 += get_value(character)
        set = []

print("result first  puzzle:", total)
print("result second puzzle:", total2)
