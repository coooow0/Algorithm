import sys
input = sys.stdin.readline

line = list(input().strip().split('-'))

for i in range(len(line)):
    nums = line[i].replace('+', ' ')
    nums = list(map(int, nums.split(' ')))
    if len(nums) == 1:
        line[i] = int(nums[0])
    else:
        res = 0
        for k in range(len(nums)):
            res += int(nums[k])
        line[i] = res
    
ans = line[0]
for i in range(1, len(line)):
    ans -= line[i]
print(ans)