n = input()
arr=[]
for i in n:
    arr.append(i)
arr.sort(reverse=True)
print(''.join(arr))