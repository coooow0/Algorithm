a = list(map(int, input().split()))
result = sum([pow(i, 2) for i in a]) % 10
print(result)
