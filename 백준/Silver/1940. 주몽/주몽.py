n = int(input()) # 재료의 개수 
m = int(input())

arr = list(map(int, input().split()))
# 두 재료의 합이 m이 되면 갑옷을 만들 수 있음. 몇개가 되는가
arr.sort()
cnt = 0

start = 0
end = n - 1
# 투포인터는 while, start, end가 자주 쓰임.. 파이팅 
while arr[start] < arr[end]:
    if arr[start] + arr[end] > m:
        end -= 1
    elif arr[start] + arr[end] < m:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1
print(cnt)