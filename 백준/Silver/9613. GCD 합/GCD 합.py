def gcd(a, b): #최대공약수
    if a < b:
        a, b = b, a #더 클 경우 바꿔줌
    
    while b > 0:
        c = a % b
        a, b = b, c
        
    return a

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(1, arr[0] + 1):
        for k in range(i+1, arr[0] + 1):
            answer += gcd(arr[i], arr[k])
    print(answer)