import sys
input = sys.stdin.readline

arr = {'l' : 1, 'k': 1, 'p': 1}

for _ in range(3):
    line = input().strip()
    if line[0] in arr:
        del arr[line[0]]
    
print('GLOBAL' if len(arr) == 0 else 'PONIX')