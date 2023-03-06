class monkey:
    def __init__(self, items, operation, test, throw):
        self.items = items
        self.operation = operation
        self.test = test
        self.throw = throw
        self.inspect = 0

    def insp(self):
        if self.items == []: return
        self.inspect += 1
        if (self.operation[1] == 'old'): increase = self.items[0]
        else: increase = int(self.operation[1])
        if (self.operation[0] == '+'): self.items[0] = self.items[0] + increase
        elif (self.operation[0] == '*'): self.items[0] = self.items[0] * increase

    def test_item(self):
        if self.items == []: return
        if (self.items[0]%self.test == 0): return True
        else: return False

    def throw_item(self, monkeys):
        if self.items == []: return
        to = self.throw[self.test_item()]
        monkeys[to].items.append(self.items[0])
        del self.items[0]

    def print(self):
        print(self.inspect, end = ' ')

def x_rounds(x, monkeys, relax):
    common = 1
    for monkey in monkeys: common *= monkey.test
    for i in range(x):
        for monkey in monkeys:
            while monkey.items != []:
                monkey.insp()
                if relax: monkey.items[0] = monkey.items[0]//3
                else: monkey.items[0] = monkey.items[0]%common
                monkey.throw_item(monkeys)

    first, second = 0, 0
    for monkey in monkeys:
        if monkey.inspect > first:
            second = first
            first = monkey.inspect
        elif monkey.inspect > second:
            second = monkey.inspect
    return(first*second)

file = open("input.txt", "r")
lines = file.read()

monkeys1 = []
monkeys2 = []
for partition in lines.split("\n\n"):
    partition = partition.split("\n")
    items = [int(x) for x in partition[1].split(": ")[1].split(", ")]
    operation = partition[2].split(" ")[-2:]
    test = int(partition[3].split(" by ")[1])
    throw = (int(partition[5].split(" monkey ")[1]), int(partition[4].split(" monkey ")[1]))
    monkeys1.append(monkey(items.copy(), operation, test, throw))
    monkeys2.append(monkey(items.copy(), operation, test, throw))

print ("result first  puzzle:", x_rounds(20, monkeys1, 1))
print ("result second puzzle:", x_rounds(10000, monkeys2, 0))
