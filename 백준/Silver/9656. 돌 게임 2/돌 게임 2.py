
n = int(input())

if n < 3:
    if n == 1:
        print('CY')
    else:
        print('SK')
else:
    if n % 2 == 0:
        print('SK')
    else:
        print('CY')
        