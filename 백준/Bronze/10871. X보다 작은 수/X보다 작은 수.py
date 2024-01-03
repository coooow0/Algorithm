n, x = map(int, input().split())
Li = list(map(int, input().split()))
for i in range(n):
    if Li[i] < x:
        print(Li[i], end=" ")