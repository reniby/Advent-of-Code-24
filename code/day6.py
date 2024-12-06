import time

starttime = time.time()

map = []
start = (0,0)
with open('inputs/day6.txt', 'r') as file:
    lineCount = 0
    for line in file:
        line = line.strip()

        temp = []
        for c in range(len(line)):
            if line[c] == "^":
                start = (lineCount, c)
            temp.append(line[c])
        map.append(temp)

        lineCount += 1

directions = [(-1,0), (0,1), (1,0), (0,-1)]
dir = 0
seen = []
path = []

i = start[0] - 1
j = start[1]
while i >= 0 and i < len(map) and j >= 0 and j < len(map[i]):
    if map[i][j] == '#':
        i -= directions[dir][0]
        j -= directions[dir][1]
        dir = (dir + 1) % 4
    else:
        path.append([i,j,dir%4])
        if (i,j) not in seen: seen.append((i,j))
    
    i += directions[dir][0]
    j += directions[dir][1]

print(len(seen))

loops = 0
pathCount = 0
for seeni, seenj in seen:
    map[seeni][seenj] = '#'

    i, j, dir = path[pathCount][0], path[pathCount][1], path[pathCount][2]

    loopCheck = set()

    while 0 <= i < len(map) and 0 <= j < len(map[i]):
        if (i, j, dir) in loopCheck:
            loops += 1
            break
        
        if map[i][j] == '#':
            i -= directions[dir][0]
            j -= directions[dir][1]
            dir = (dir + 1) % 4
        
        loopCheck.add((i, j, dir))
        
        i += directions[dir][0]
        j += directions[dir][1]
    
    map[seeni][seenj] = '.'
    pathCount += 1

print(loops)

endtime = time.time()
print(endtime-starttime)