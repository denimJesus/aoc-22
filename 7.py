file = open("7.txt")

commands = []
command = ""
valid_dirs = []
global active

while True:
    line = file.readline()
    if not line: break
    if line[-1] == '\n': line = line[:-1]
    commands.append(iter(line.split()))
file.close()


class Node:
    def __init__(self, name = "", parent = None, size = 0):
        self.name = name
        self.parent = parent
        self.size = size
        self.content = []

    def ls(self):
        pass

    def md(self, name = "", size = 0):
        newnode = Node(name, self, size)
        self.content.append(newnode)
        return newnode
        
    def cd(self, name):
        global active
        if name == "/":
            active = root
        elif name == "..":
            active = self.parent
        else:
            index = self.search_for_index(name)
            active = self.content[index]
        
    def search_for_index(self, query):
        for _ in range(len(self.content)):
            if self.content[_].name == query: return _


root = Node("root")
active = root

for _ in range(len(commands)):
    command = next(commands[_])
    if command == "$":
        command = next(commands[_])
        if command == "ls":
            continue
        elif command == "cd":
            active.cd(next(commands[_]))
    elif command == "dir":
        active.md(next(commands[_]))
    else:
        active.md(next(commands[_]), command)

# 7.1
global answer
answer = 0

def get_sizes(dir):
    dirsize = 0
    for _ in dir.content:
        if not _.size:
            get_sizes(_)
            dirsize += int(_.size)
        else:
            dirsize += int(_.size)        
    
    dir.size = dirsize
    

    
    if 0 < dir.size <= 100000:
        valid_dirs.append(dir)
    
get_sizes(root)

for _ in valid_dirs:
    answer += _.size
 
print(answer)
print()

# 7.2
target = 30_000_000 - (70_000_000 - root.size)
answer = 70_000_000
valid_dirs = []

def get_smallest_valid(dir):
    global answer
    for _ in dir.content:
        if not _.content == []:
            get_smallest_valid(_)
            if int(_.size) >= target and int(_.size) < answer and _.content != []: 
                answer = _.size

get_smallest_valid(root)
print(answer)