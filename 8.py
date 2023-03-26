# 8.1
file = open("8.txt")
arr = []
appended = False
answer = 0
tallest = 0


class Tree():
    def __init__(self, h):
        self.h = h
        self.visible = False

while True:
    line = file.readline()
    if not line: break
    if line[-1] == '\n': line = line[:-1]
    for _ in range(len(line)):
        if not appended: arr.append([])
        arr[_].append(Tree(int(line[_])))
    appended = True
file.close()

for n in range(len(arr)):
    arr[n][0].visible, arr[n][-1].visible = True, True
    tallest = arr[n][0].h
    for m in range(len(arr[n])):
        if arr[n][m].h > tallest:
            arr[n][m].visible = True
            tallest = arr[n][m].h
        if tallest == 9: break

    tallest = arr[n][-1].h
    for m in range(len(arr[n])-1, -1, -1):
        if arr[n][m].h > tallest:
            arr[n][m].visible = True
            tallest = arr[n][m].h
        if tallest == 9: break
        
for n in range(len(arr)):
    arr[0][n].visible, arr[-1][n].visible = True, True
    tallest = arr[0][n].h
    for m in range(len(arr[n])):
        if arr[m][n].h > tallest:
            arr[m][n].visible = True
            tallest = arr[m][n].h
        if tallest == 9: break
        
    tallest = arr[-1][n].h
    for m in range(len(arr[n])-1, -1, -1):
        if arr[m][n].h > tallest:
            arr[m][n].visible = True
            tallest = arr[m][n].h
        if tallest == 9: break
        
for n in arr:
    for m in n:
        if m.visible == True: answer += 1
        
print(answer)
print()

# 8.2
answer = 0

for n in range(len(arr)):
    for m in range(len(arr[n])):
        scene_arr = [0, 0, 0, 0]
        arr[n][m].scenic = 0
        tallest = 0
        
        for _ in range(m-1, -1, -1):
            if arr[_][n].h > tallest:
                tallest = arr[_][n].h
            scene_arr[0] += 1            
            if tallest >= arr[m][n].h:
                break
        tallest = 0
        for _ in range(n-1, -1, -1):
            if arr[m][_].h > tallest:
                tallest = arr[m][_].h
            scene_arr[1] += 1
            if tallest >= arr[m][n].h:
                break
        tallest = 0
        for _ in range(m+1, len(arr)):
            if arr[_][n].h > tallest:
                tallest = arr[_][n].h
            scene_arr[2] += 1
            if tallest >= arr[m][n].h:
                break
        tallest = 0
        for _ in range(n+1, len(arr[n])):
            if arr[m][_].h > tallest:
                tallest = arr[m][_].h
            scene_arr[3] += 1
            if tallest >= arr[m][n].h:
                break
        arr[m][n].scenic = scene_arr[0] * scene_arr[1] * scene_arr[2] * scene_arr[3]
        if arr[m][n].scenic > answer: answer = arr[m][n].scenic

print(answer)