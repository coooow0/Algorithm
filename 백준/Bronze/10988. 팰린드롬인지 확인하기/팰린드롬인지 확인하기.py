a = input()
a = list(a)
if a == list(reversed(a)):
    print(1)
else:
    print(0)


# a.reverse 를 사용했었는데 오류가 나는 이유
# 위 코드는 a의 원본을 뒤집은 상태로 만들고, 반환값은 none이다. 
# 그래서 a == a.reverse()가 항상 false로 나왔던 것
# 따라서 원본을 변경하지 않고 뒤집는 함수인 list(reversed(a))를 사용해야 한다.