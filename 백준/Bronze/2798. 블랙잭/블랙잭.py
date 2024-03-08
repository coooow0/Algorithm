from itertools import combinations

n, m = map(int, input().split())
#n은 카드의 개수, m은 넘지 말아야 하는 수
arr = list(map(int, input().split()))
result = []

for i in combinations(arr, 3):
    if sum(i) > m:
        continue
    else:
        result.append(sum(i))

print(max(result))

# combinations(a, n)
# a에 반복문이나 리스트 등의 반복 가능한 것을 넣음
# n에 중복을 허용하지 않고 뽑을 개수를 넣음
