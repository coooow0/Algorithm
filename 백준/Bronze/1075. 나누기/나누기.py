n = input()
f = int(input())

for i in range(0, 100):
    if i < 10:
        n = n[:len(n)-2] + '0' +str(i)
        
    else:
        n = n[:len(n)-2] + str(i)
        
    
    if int(n) % f == 0:
        print('0' + str(i) if i < 10 else i)
        break