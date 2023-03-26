# 1.1
file = open("1.txt")
arr = []
line = ""
_sum = 0

while True:
    line = file.readline()
    if not line: break
    if line != '' and line != '\n':
        _sum += int(line)
    else:
        arr.append(_sum)
        _sum = 0

print(max(arr))
print()

# 1.2
_sum = 0
arr.sort()
for _ in arr[-1:-4:-1]:
    _sum += _
print(_sum)

file.close()