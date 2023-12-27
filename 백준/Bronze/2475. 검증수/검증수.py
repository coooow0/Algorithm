a = list(map(int, input().split()))
result = 0
for i in range(len(a)):
    result = result + a[i] * a[i]
print(result%10)