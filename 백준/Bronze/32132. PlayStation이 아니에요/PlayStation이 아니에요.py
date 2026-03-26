import sys
input = sys.stdin.readline

n = int(input().strip())
arr = input().strip()

while True:
    if 'PS4' in arr or 'PS5' in arr:
        arr = arr.replace('PS4', 'PS').replace('PS5', 'PS')
    else:
        break
    
print(arr)

