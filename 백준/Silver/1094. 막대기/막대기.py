cnt = 0
arr = []
for i in range(7):
    arr.append(2 ** i)
arr.sort(reverse=True)

x = int(input())

for num in arr:
    if x >= num:
        x -= num
        cnt += 1
        
    if x == 0:
        break
print(cnt)