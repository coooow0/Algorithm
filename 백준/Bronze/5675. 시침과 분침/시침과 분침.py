import sys
input = sys.stdin.readline

while True:
    try:
        time = int(input().strip())
        
        if time % 12 == 6 or time % 12 == 0:
            print('Y')
        else:
            print('N')
    except:
        exit()
