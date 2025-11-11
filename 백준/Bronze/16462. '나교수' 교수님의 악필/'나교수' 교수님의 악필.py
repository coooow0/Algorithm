import math
import sys
input = sys.stdin.readline

n = int(input())

cnt = 0

for _ in range(n):
    num = input().strip()
    
    if num == '100':
        cnt += 100
    else:   
        string = ''
        arr = list(num)
        for i in range(len(arr)):
            if arr[i] in ['6', '0']:
                arr[i] = '9'
        
        for i in arr:
            string += i
        
        cnt += int(string)
        
print(math.floor(cnt / n + 0.5))