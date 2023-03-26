#2.1
file = open("2.txt")
arr1 = []
arr2 = []

global score
score = 0

while True:
    line = file.readline()
    if not line: break
    arr1.append(line[0])
    arr2.append(line[-2])
file.close()
       
for _ in range(len(arr1)):
    if arr1[_] == 'A':
        if arr2[_] == 'X': score += 3
        elif arr2[_] == 'Y': score += 6
        else: pass
    elif arr1[_] == 'B':
        if arr2[_] == 'Y': score += 3
        elif arr2[_] == 'Z': score += 6
        else: pass
    else:
        if arr2[_] == 'Z': score += 3
        elif arr2[_] == 'X': score += 6
        else: pass
    if arr2[_] == 'X': score += 1
    elif arr2[_] == 'Y': score += 2
    else: score += 3

print(score)
print()

#2.2
score = 0
for _ in range(len(arr1)):
    if arr2[_] == 'X':
        if arr1[_] == 'A': score += 3
        elif arr1[_] == 'B': score += 1
        else: score += 2
    elif arr2[_] == 'Y':
        score += 3
        if arr1[_] == 'A': score += 1
        elif arr1[_] == 'B': score += 2
        else: score += 3
    else:
        score += 6
        if arr1[_] == 'A': score += 2
        elif arr1[_] == 'B': score += 3
        else: score += 1

print(score)