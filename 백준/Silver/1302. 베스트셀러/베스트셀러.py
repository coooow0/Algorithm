# 베스트셀러
n = int(input())
arr = dict()
for _ in range(n):
    book = input()
    if book not in arr:
        arr[book] = 1
    else:
        arr[book] += 1
sorted(arr)
# print(arr)
cnt = max(arr.values())

# print(count)
best = []

for name, count in arr.items():
    if cnt == count:
        best.append(name)
        
print(sorted(best)[0])


