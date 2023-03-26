# 9.1
file = open("9.txt")
visited = set()
moves = []
head_coord = [0, 0]
tail_coord = [0, 0]

while True:
    line = file.readline().split()
    if not line: break
    moves.append(line)
file.close()

for command, times in moves:
    if command == 'U':
        head_coord[1] += int(times)
    elif command == 'D':
        head_coord[1] -= int(times)
    elif command == 'L':
        head_coord[0] -= int(times)
    elif command == 'R':
        head_coord[0] += int(times)
 
    while abs(head_coord[0] - tail_coord[0]) > 1 or abs(head_coord[1] - tail_coord[1]) > 1:
        visited.add((tail_coord[0], tail_coord[1]))
        
        if head_coord[0] - tail_coord[0] > 0:
                tail_coord[0] += 1
        elif head_coord[0] - tail_coord[0] < 0:
                tail_coord[0] -= 1
                
        if head_coord[1] - tail_coord[1] > 0:
                tail_coord[1] += 1
        elif head_coord[1] - tail_coord[1] < 0:
                tail_coord[1] -= 1
                
visited.add((tail_coord[0], tail_coord[1]))

print(len(visited))
print()

# 9.2
visited = set()
coords = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited.add((0, 0))

def drag():
    for _ in range(1, 10):
        while abs(coords[_-1][0] - coords[_][0]) > 1 or abs(coords[_-1][1] - coords[_][1]) > 1:
                    
            if coords[_-1][0] - coords[_][0] > 0:
                    coords[_][0] += 1
            elif coords[_-1][0] - coords[_][0] < 0:
                    coords[_][0] -= 1
                    
            if coords[_-1][1] - coords[_][1] > 0:
                    coords[_][1] += 1
            elif coords[_-1][1] - coords[_][1] < 0:
                    coords[_][1] -= 1
                
            if _ == 9: visited.add((coords[9][0], coords[9][1]))


for command, times in moves:
    if command == 'U':
        for _ in range(int(times)):
            coords[0][1] += 1
            drag()
    elif command == 'D':
        for _ in range(int(times)):
            coords[0][1] -= 1
            drag()
    elif command == 'L':
        for _ in range(int(times)):
            coords[0][0] -= 1
            drag()
    elif command == 'R':
        for _ in range(int(times)):
            coords[0][0] += 1
            drag()
                
print(len(visited))