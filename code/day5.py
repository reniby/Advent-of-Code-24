
phase = 0
rules = {}
part1 = 0
part2 = 0
with open('inputs/day5.txt', 'r') as file:
    for line in file:
        line = line.strip()
        valid = True

        if line == "":
            phase = 1
        elif not phase:
            if int(line[:2]) not in rules: 
                rules[int(line[:2])] = []
            rules[int(line[:2])].append(int(line[3:]))
        elif phase:
            line = line.split(",")
            update = []

            for i in line:
                update.append(int(i))
        
            prev = []
            for i in update:
                for j in rules.get(i, []):
                    if j in prev:
                        valid = False
                prev.append(i)
            if valid:
                part1 += int(line[int(len(line)/2)])
            else:
                while not valid:
                    valid = True
                    prev = []
                    for i in range(len(update)):
                        for j in range(len(rules.get(update[i], []))):
                            #print(prev, i, j, update[i], rules[update[i]])
                            if rules[update[i]][j] in prev:
                                #print(update[i], update[:i], update[i+1:])
                                update = [update[i]] + update[:i] + update[i+1:]
                                valid = False
                                break
                        prev.append(update[i])

                part2 += int(update[int(len(update)/2)])
                
            


print(part1)
print(part2)

