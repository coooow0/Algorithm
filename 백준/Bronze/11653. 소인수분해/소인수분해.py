n = int(input())
i = 2
while i * i <= n:
    while n % i == 0:  # i로 나누어 떨어질 때까지 나눔
        print(i)
        n //= i
    i += 1
# 남은 n이 1보다 크면 소수이므로 출력
if n > 1:
    print(n)
