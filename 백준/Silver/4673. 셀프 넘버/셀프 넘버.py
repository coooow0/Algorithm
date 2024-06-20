def d(n):
    new_n = n
    # 각 자리수를 더함
    for num in str(n):
        new_n += int(num) 
    return new_n

arr = [i for i in range(1, 10001)]
for i in range(10001):
    if d(i) in arr:
        arr.remove(d(i))

for i in arr:
    print(i)