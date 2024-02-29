import sys

input = sys.stdin.readline
n = int(input())
List = []

for _ in range(n):
    List.append(int(input()))

List.sort()

print('\n'.join(map(str, List)))
