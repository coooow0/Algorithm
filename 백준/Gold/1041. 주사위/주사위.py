import sys
input = sys.stdin.readline

from itertools import combinations

n = int(input().strip())

arr = list(map(int, input().strip().split()))

dame = [(0, 5), (1, 4), (2, 3)]

two = 1000000000000000

if n == 1:
    res = 1000000000000000
    for c in combinations([i for i in range(6)], 5):
        if any([a in c and b in c for a, b in dame]):
            
            tmp = sum([arr[k] for k in c])
            res = min(tmp, res)
    print(res)
    exit()
            

for c in combinations([j for j in range(6)], 2):
    if not any([a in c and b in c for a, b in dame]):
        tmp = sum([arr[k] for k in c])
        two = min(tmp, two)
        
# for c in combinations(arr, 2):
#     if not any([arr[i] in c and arr[j] in c for i, j in dame]):
#         two = min(two, sum(c))
        
three = 1000000000000000

for c in combinations([j for j in range(6)], 3):
    if not any([a in c and b in c for a, b in dame]):
        tmp = sum([arr[k] for k in c])
        three = min(tmp, three)
        

# for c in combinations(arr, 3):
#     if not any([arr[i] in c and arr[j] in c for i, j in dame]):
#         three = min(three, sum(c))
one = min(arr)

top = (three * 4) + (two * ((n - 2) * 4)) + one *(n ** 2 - 4 - (n -2) * 4)
bottom = (two * 4) + one *((n - 2) * 4)

print(top + bottom * (n - 1))