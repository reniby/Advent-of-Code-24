
left = []
right = []

with open('inputs/day1.txt', 'r') as file:
    for line in file:
        line = line.strip().split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))

left.sort()
right.sort()
part1 = 0
for i in range(len(left)):
    part1 += abs(left[i]-right[i])

hm = {}
part2 = 0
for i in right:
    hm[i] = hm.get(i, 0) + 1

for i in left:
    part2 += int(i * hm.get(i, 0))

print(part1)
print(part2)