s = int(input())
# 서로 다른 n개의 자연수 합이 s.
# s를 알 때 자연수 n의 최댓값은?
ans = 0
for i in range(1, 1000000):
    ans += i
    
    if ans > s:
        print(i - 1) 
        break
    