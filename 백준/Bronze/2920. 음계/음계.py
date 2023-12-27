a = list(map(int, input().split()))
# sort는 원래 리스트를 정렬하는데 sorted는 원래 리스트는 냅두고 잠시 정렬
if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    #reverse=False면 오름차순 정렬 즉 첫 값이 작은 거
    #reverse=True면 내림차순 정렬 즉 첫 값이 큰 것
    print('descending')
else:
    print('mixed')