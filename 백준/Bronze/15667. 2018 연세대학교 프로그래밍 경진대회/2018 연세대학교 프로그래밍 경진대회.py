n = int(input())
n -= 1

for i in range(1, n + 1):
    if (n - i) // i == i:
        print(i)
        exit()