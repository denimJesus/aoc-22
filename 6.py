# 6.1
file = open("6.txt")
count = 4
found = False
line = file.readline()
file.close()

tempstr = line[:4]
while not found:
    count += 1
    tempstr = tempstr[1:] + line[count-1]
    if tempstr.count(tempstr[0]) == 1 and tempstr.count(tempstr[1]) == 1 and tempstr.count(tempstr[2]) == 1 and tempstr.count(tempstr[3]) == 1:
        found = True
        break

print(count)
print()

# 6.2
count = 14
found = False
tempstr = line[:14]
while not found:
    count += 1
    tempstr = tempstr[1:] + line[count-1]
    for c in tempstr:
        if tempstr.count(c) > 1:
            break
    else: found = True

print(count)