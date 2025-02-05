switch = int(input()) # 스위치 개수
light = list(map(int, input().split())) #스위치 상태

std = int(input()) # 학생 수 
for _ in range(std):
    gender, number = list(map(int, input().split()))
    
    if gender == 1: # 남학생의 경우
        for i in range(1, switch // number + 1):
            idx = i * number - 1
            light[idx] = 1 - light[idx]
        
    else: # 여학생의 경우
        number -= 1
        light[number] = 1 - light[number]
        # 여학생이 받은 수의 위치를 추가함.. 
        for i in range(1, switch):
            left = number - i
            right = number + i
            if left < 0 or right >= switch or light[left] != light[right]:
                break
            
            light[left] = 1 - light[left]
            light[right] = 1 - light[right]
        
for i in range(switch):
    print(light[i], end=' ')
    if (i + 1) % 20 == 0:
        print()