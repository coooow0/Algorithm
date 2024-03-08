import sys
n = int(sys.stdin.readline())
A = set(map(int, input().split()))

m = int(sys.stdin.readline())
B = list(map(int, input().split()))

for i in B:
    print(1) if i in A else print(0)
    # 만약 i가 A안에 있다면 print(1)
    # 없으면 print(0)