n, m = map(int, input().split())
#n은 카드의 개수, m은 넘지 말아야 하는 수
arr = list(map(int, input().split()))
result = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = arr[i] + arr[j] + arr[k]
            if sum > m:
                continue
            else:
                result.append(sum)
print(max(result))