import sys
input = sys.stdin.readline

k, s, n = map(str, input().strip().split())
n = int(n)

arr = []

dic = {'L': [0, -1], 'R': [0, 1], 'T': [-1, 0], 'B': [1, 0], 
       'LT':[-1, -1], 'LB': [1, -1], 'RT':[-1, 1], 'RB': [1, 1]}

for i in [k, s]:
    arr.append([8 - int(i[1]), ord(i[0]) - 65])
king = arr[0]
stone = arr[1]

for _ in range(n):
    line = input().strip()
    
    a, b = dic[line]
    
    king[0] += a
    king[1] += b
    
    if king[0] < 0 or king[0] > 7 or king[1] < 0 or king[1] > 7:
        king[0] -= a
        king[1] -= b
        
    elif king == stone:
        stone[0] += a
        stone[1] += b
        
        if stone[0] < 0 or stone[0] > 7 or stone[1] < 0 or stone[1] > 7:
            stone[0] -= a
            stone[1] -= b
            
            king[0] -= a
            king[1] -= b
        
    

print(chr(king[1] + 65), 7 - king[0] + 1, sep='')
print(chr(stone[1] + 65), 7 - stone[0] + 1, sep='')