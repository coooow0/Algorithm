n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0 # 최종 결과를 나타냄 
result = 0

for i in range(len(arr)):
    result += arr[i]
    answer += result
print(answer)