file = open("input.txt", "r")
lines = file.read()

for line in lines.split("\n")[0:-1]:
    print(line)

print ("result first  puzzle:", "not started")
print ("result second puzzle:", "not started")
