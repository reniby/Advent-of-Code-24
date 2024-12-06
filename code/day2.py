def checkArr(arr):
    dir = arr[0] < arr[1]
    for i in range(1, len(arr)):
        if dir != (arr[i-1] < arr[i]):
            return i
        if abs(arr[i] - arr[i-1]) > 3 or abs(arr[i] - arr[i-1]) == 0:
            return i
    return -1

with open('inputs/day2.txt', 'r') as file:
    part2 = 0
    part1 = 0
    for line in file:
        line = line.strip().split()
        safe = False
        for c in range(len(line)):
            line[c] = int(line[c])

        part1 += checkArr(line) == -1

        for c in range(len(line)):
            check = checkArr(line[:c]+line[c+1:])
            if check == -1: safe = True
        part2 += safe
    
print(part1)
print(part2)
