import sys

input = sys.stdin.readline
n = int(input())
List = list()

for i in range(n):
    a = int(input())
    List.append(a)

List.sort()
for i in range(n):
    print(List[i])