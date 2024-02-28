t = int(input())
for i in range(t):
    n = list(map(str, input().split()))
    sp = list(n[1])
    for j in range(len(sp)):
        print(int(n[0])*sp[j], end="")
    print()
    