import sys
input = sys.stdin.readline

arr = list(map(int, input().strip().split()))

arr.sort()
print(min(arr[0], arr[1]) * min(arr[2], arr[3]))
