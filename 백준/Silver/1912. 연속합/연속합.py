n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    a[i] = max(a[i], a[i-1] + a[i])
    # '연속된' 누적 합 중 제일 큰 수를 구하는 것이기 때문에.. dp는 필요없다
print(max(a))