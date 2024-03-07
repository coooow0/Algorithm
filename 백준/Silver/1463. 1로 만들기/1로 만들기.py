n = int(input())

dp = [0] * (n+1) 
# dp[1] = 1을 연산한 횟수를 배열 안 값에 집어 넣음. 따라서 n+1만큼의 배열이 필요하다.  ex) dp[10] = 3 
for i in range(2, n+1):
    # 어차피 d[0], d[1]의 값은 0이기 때문에 2부터 시작함
    dp[i] = dp[i-1] + 1 # 연산 횟수를 더해준다. 앞 배열의 값을 참조함

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    # elif가 아니라 if인 이유 = 6의 배수도 있기 때문에
        
print(dp[n])