a = list(map(int, input().split()))
result = 0
for i in range(len(a)):
    result = result + pow(a[i], 2)
print(result%10)