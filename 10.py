# 10.1
file = open("10.txt")
arr = []
x = 1
cycle = 0
signals = []
skip = False

while True:
    line = file.readline()
    if not line: break
    if line[-1] == '\n': line = line[:-1]
    command = line.split(' ')
    if len(command) == 1: command.append('0')
    arr.append(command)
file.close()

for com, v in arr:
    
    if (cycle + 20) % 40 == 0 and not skip:
        signals.append(cycle*x)
    skip = False
    cycle += 1

    if com == "addx":
        if (cycle + 20) % 40 == 0:
            signals.append(cycle*x)
        cycle += 1
        if (cycle + 20) % 40 == 0:
            signals.append(cycle*x)
            skip = True
    
    x += int(v)    
   
print(sum(signals))

# 10.2
x = 1
cycle = 0
pixels = []
delay = 0
output = ""

for com, v in arr:
    
    if com == "addx":
        delay = 1
    while delay > 0:
        delay -= 1
        if abs(x - (cycle - 40 * (cycle // 40))) <= 1:
            pixels.append(True)
        else: pixels.append(False)
        cycle += 1
    if abs(x - (cycle - 40 * (cycle // 40))) <= 1:
        pixels.append(True)
    else: pixels.append(False)
    x += int(v)
        
    cycle += 1
    
for _ in range(len(pixels)):
    if _ % 40 == 0: output += '\n'
    output = output + "#" if pixels[_] == True else output + "."
    
print(output)