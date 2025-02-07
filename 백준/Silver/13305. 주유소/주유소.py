n = int(input())
kilo = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]

result = 0

for i in range(n - 1):
    if min_price > price[i]:
        min_price = price[i]
    result += min_price * kilo[i]
print(result)