# 3.1
file = open("3.txt")
arr1 = []
arr2 = []
both = []
_sum = 0
i = 0

while True:
    str1 = ""
    str2 = ""
    line = file.readline()
    if not line: break
    mid = len(line)//2
    for _ in range(mid):
        str1 += line[_]
        str2 += line[_+mid]
    arr1.append(str1)
    arr2.append(str2)
file.close()

for word in arr1:
    for c in word:
        if c in arr2[i]:
            both.append(c)
            break
    i += 1

for _ in both:
    if ord(_) < 95:
        _sum += ord(_)-38
    else: 
        _sum += ord(_)-96

print(_sum)
print()

#3.2
file = open("3.txt")
arr = [[],[],[]]
in_all = []
_sum = 0
i = 0

while True:
    line = file.readline()
    if not line: break
    if line[-1] == '\n': line = line[:-1]
    arr[i].append(line)
    i = i + 1 if i < 2 else 0
file.close()

for _ in arr[0]:
    for c in _:
        if c in arr[1][i] and c in arr[2][i]:
            in_all.append(c)
            i += 1
            break
            
for _ in in_all:
    if ord(_) < 95:
        _sum += ord(_)-38
    else: 
        _sum += ord(_)-96

print(_sum)