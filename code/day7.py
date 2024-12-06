
def plusormul(nums, idx, op, curr, testValue):
    if op == '+':
        curr += int(nums[idx])
    else:
        curr *= int(nums[idx])
    if idx == len(nums) - 1:
        return curr == testValue
    return plusormul(nums, idx+1, '+', curr, testValue) or plusormul(nums, idx+1, '*', curr, testValue)

def orconcat(nums, idx, op, curr, testValue):
    if op == '+':
        curr += int(nums[idx])
    elif op == '*':
        curr *= int(nums[idx])
    else:
        curr = int(str(curr) + nums[idx])
    if idx == len(nums) - 1:
        return curr == testValue
    return orconcat(nums, idx+1, '+', curr, testValue) or orconcat(nums, idx+1, '*', curr, testValue) or orconcat(nums, idx+1, '|', curr, testValue)

part1 = 0
part2 = 0
with open('inputs/day7.txt', 'r') as file:
    for line in file:
        line = line.strip().split(" ")
        testValue = int(line[0][:-1])
        nums = line[1:]

        plus = plusormul(nums, 0, '+', 0, testValue)
        mul = plusormul(nums, 0, '*', 0, testValue)
        part1 += (plus or mul) * testValue
        
        plus = orconcat(nums, 0, '+', 0, testValue)
        mul = orconcat(nums, 0, '*', 0, testValue)
        concat = orconcat(nums, 0, '|', 0, testValue)
        part2 += (plus or mul or concat) * testValue

print(part1)
print(part2)

        
