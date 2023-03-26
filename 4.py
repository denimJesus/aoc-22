# 4.1
file = open("4.txt")
arr = []
temparr= []
count = 0
valid = True

while True:
    line = file.readline()
    if not line: break
    if line[-1] == "\n": line = line[:-1]
    for _ in line.split(","):
        temparr = _.split("-")
        arr.append((int(temparr[0]), int(temparr[1])))
file.close()

for _ in range(len(arr)//2):
    valid = True
    ran1 = range(arr[_*2][0], arr[_*2][1]+1)
    ran2 = range(arr[_*2+1][0], arr[_*2+1][1]+1)
    for n in ran1:
        if n not in ran2:
            for m in ran2:
                if m not in ran1:
                    valid = False
                    break
                else: continue
    if valid: count += 1

print(count)
print()

# 4.2
count = 0
for _ in range(len(arr)//2):
    valid = False
    ran1 = range(arr[_*2][0], arr[_*2][1]+1)
    ran2 = range(arr[_*2+1][0], arr[_*2+1][1]+1)
    for n in ran1:
        if n in ran2: valid = True
    if valid: count += 1

print(count)