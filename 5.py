# 5.1
file = open("5.txt")
lines = []
times = []
_from = []
to = []
arr = [[],[],[],[],[],[],[],[],[]]
temparr = []
i = 0

for _ in range(8):
    line = file.readline()
    if not line: break
    if line[-1] == '\n': line = line[:-1]
    lines.append(line)

while True:
    line = file.readline()
    if not line: break
    if line[:4] != "move": continue
    if line[-1] == '\n': line = line[:-1]
    temparr = line.split()
    times.append(temparr[1])
    _from.append(int(temparr[3])-1)
    to.append(int(temparr[5])-1)
file.close()

temparr = [[],[],[],[],[],[],[],[],[]]
for _ in range(7,-1,-1):
    i = 0
    for n in lines[_][1::4]:
        if n != " ":
            arr[i].append(n)
            temparr[i].append(n)
        i += 1

for _ in range(len(times)):
    for n in range(int(times[_])):
        arr[to[_]].append(arr[_from[_]].pop())
for _ in arr:
    print(_[-1])
print()

# 5.2
arr = temparr
for _ in range(len(times)):
    temparr = []
    for n in range(int(times[_])):
        temparr.append(arr[_from[_]].pop())
    arr[to[_]] += (temparr[::-1])

for _ in arr:
    print(_[-1])