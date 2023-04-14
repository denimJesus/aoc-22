# 11.1
file = open("11.txt")
round = 0
monkeys = []
linecount = -1
stats = []
operation = 0

class Monkey():
    def __init__(self, items = [], oper = [], test = 0, if_true = -1, if_false = -1):
        self.items = items
        self.oper = oper
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0
        monkeys.append(self)

while True:
    line = file.readline()
    temp = []
    if not line: 
        Monkey(stats[0], stats[1], stats[2], stats[3], stats[4])
        break
    if line[-1] == "\n": line = line[:-1]
    linecount += 1
    if linecount == 0: continue
    elif linecount == 1:
        temp = line.split()[2:]
        for _ in range(len(temp)):
            if temp[_][-1] == ",": temp[_] = int(temp[_][:-1])
            else: temp[_] = int(temp[_])
        stats.append(temp)  
    elif linecount == 2:
        temp = line.split()[-2:]
        stats.append(temp)
    elif linecount in [3, 4, 5]:
        stats.append(int(line.split()[-1]))
    elif linecount == 6:
        linecount = -1
        Monkey(stats[0], stats[1], stats[2], stats[3], stats[4])
        stats = []
file.close()

while round < 20:
    round += 1
    for m in monkeys:
        for item in m.items:
            m.inspections += 1
            operation = int(item) if m.oper[1] == "old" else int(m.oper[1])
            if m.oper[0] == "+":
                item += operation
            elif m.oper[0] == "*":
                item *= operation
            item //= 3
            if item % m.test == 0:
                monkeys[m.if_true].items.append(item)
            else:
                monkeys[m.if_false].items.append(item)
        m.items = []
        
inspections_array = []
for m in monkeys:
    inspections_array.append(m.inspections)
inspections_array.sort(reverse = True)
print(inspections_array[0] * inspections_array[1])

# 11.2
file = open("11.txt")
round = 0
monkeys = []
linecount = -1
stats = []
operation = 0

while True:
    line = file.readline()
    temp = []
    if not line: 
        Monkey(stats[0], stats[1], stats[2], stats[3], stats[4])
        break
    if line[-1] == "\n": line = line[:-1]
    linecount += 1
    if linecount == 0: continue
    elif linecount == 1:
        temp = line.split()[2:]
        for _ in range(len(temp)):
            if temp[_][-1] == ",": temp[_] = int(temp[_][:-1])
            else: temp[_] = int(temp[_])
        stats.append(temp)  
    elif linecount == 2:
        temp = line.split()[-2:]
        stats.append(temp)
    elif linecount in [3, 4, 5]:
        stats.append(int(line.split()[-1]))
    elif linecount == 6:
        linecount = -1
        Monkey(stats[0], stats[1], stats[2], stats[3], stats[4])
        stats = []
file.close()

while round < 10000:
    print(round)
    round += 1
    for m in monkeys:
        for item in m.items:
            m.inspections += 1
            operation = int(item) if m.oper[1] == "old" else int(m.oper[1])
            if m.oper[0] == "+":
                item += operation
            elif m.oper[0] == "*":
                item *= operation
            if item % m.test == 0:
                monkeys[m.if_true].items.append(item)
            else:
                monkeys[m.if_false].items.append(item)
        m.items = []

inspections_array = []
for m in monkeys:
    inspections_array.append(m.inspections)
inspections_array.sort(reverse = True)
print(inspections_array[0] * inspections_array[1])