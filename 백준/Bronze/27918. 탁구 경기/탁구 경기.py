import sys
input = sys.stdin.readline

t = int(input())
arr = {'D': 0, 'P': 0}

for _ in range(t):
    n = input().strip()
    arr[n] += 1

    if abs(arr['D'] - arr['P']) == 2:
        print(arr['D'], end='')
        print(':', end='')
        print(arr['P'], end='')
        exit()
            
            
print(arr['D'], end='')
print(':', end='')
print(arr['P'], end='')