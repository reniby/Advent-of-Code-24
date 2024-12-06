
save = []

with open('inputs/day4.txt', 'r') as file:
    for line in file:
        line = line.strip()
        temp = []
        for c in line:
            temp.append(c)
        save.append(temp)

part1 = 0
part2 = 0
for i in range(len(save)):
    for j in range(len(save[i])):
        # i = vertical, j = horizontal
        if save[i][j] == 'X':
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    temp = ''
                    if i+di*3 >= 0 and i+di*3 < len(save) and j+dj*3 >= 0 and j+dj*3 < len(save[i]):
                        for n in range(4):
                            temp += save[i+di*n][j+dj*n]
                        part1 += temp == "XMAS"
        if save[i][j] == 'A' and i>0 and j>0 and i<len(save)-1 and j<len(save)-1:
            if save[i-1][j-1] == save[i-1][j+1] and save[i+1][j-1] == save[i+1][j+1]:
                part2 += save[i-1][j-1] + save[i+1][j-1] in ["MS", "SM"]
            elif save[i-1][j-1] == save[i+1][j-1] and save[i-1][j+1] == save[i+1][j+1]:
                part2 += save[i-1][j-1] + save[i-1][j+1] in ["MS", "SM"]

            

print(part1)
print(part2)