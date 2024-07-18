n = int(input())
akuma = '666'
cnt = 0
i = 666
while True:
    if akuma in str(i):
       cnt += 1
       if cnt == n:
           print(i)
           break 
    i += 1
