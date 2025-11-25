import sys
input = sys.stdin.readline

line = input().strip()
cnt = len(line)

arr = input().strip()
line = line.replace(arr, '')

if len(line) == cnt:
    print(0)
else:
    print(1)