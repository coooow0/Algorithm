max = 0
num = 0
for i in range(9):
    a = int(input())
    if max < a:
        max = a 
        num = i+1
print(max)
print(num)