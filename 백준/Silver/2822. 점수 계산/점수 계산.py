# 점수 계산
arr = []
for _ in range(8):
    arr.append(int(input()))

ans = [0 for _ in range(8)]

for i in range(8):
    for k in range(8):
        if arr[i] > arr[k]:
            ans[i] += 1

res = sorted(ans)[3] 

num = [] # 순서 저장
avg = 0 # 평균값
for i in range(8):
    if ans[i] >= res:
        num.append(i + 1)
        avg += arr[i]
print(avg)
print(*num)
     