arr = []
m = 0

for i in range(9):
    digit = int(input())
    arr.append(digit)
    if digit > m:
        m = digit
        
print(m)
print(arr.index(m) + 1)