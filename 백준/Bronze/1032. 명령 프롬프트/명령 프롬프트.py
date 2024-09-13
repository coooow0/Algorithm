n = int(input())
arr = []
for i in range(n):
    str = list(input())
    if not arr:
        arr = str
    else:
        for i in range(len(arr)):
            if str[i] != arr[i]:
                arr[i] = '?'
for i in arr:
    print(i, end='')
    