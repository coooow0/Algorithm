from collections import Counter
import sys
input = sys.stdin.readline


n = int(input().rstrip())
arr = []
for i in range(n):
    arr.append(int(input().rstrip()))

# 산술평균
print(round(sum(arr) / n))
arr.sort()

# 중앙값
print(arr[n//2])

# 최빈값
counter = Counter(arr).most_common() # 등장횟수가 많은 순으로 정렬된 리스트

max_count = counter[0][1]
many = [num for num, cnt in counter if max_count == cnt] # 등장 횟수가 같은 애들만 모아둠
many.sort()

print(many[1] if len(many) > 1 else many[0])

# 범위
print(max(arr)-min(arr))