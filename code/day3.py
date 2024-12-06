import re

with open('inputs/day3.txt', 'r') as file:
    part1 = 0
    part2 = 0
    doing = True
    for line in file:
        line = line.strip()

        regex = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
        matches = re.findall(regex, line)

        for i in matches:
            if i == "do()": 
                doing = True 
            elif i == "don't()":
                doing = False
            else:
                i = i.replace("mul(","").replace(")","").split(",")
                part1 += int(i[0]) * int(i[1])
                if doing:
                    part2 += int(i[0]) * int(i[1])
print(part1)
print(part2)
