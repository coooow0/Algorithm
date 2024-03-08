#분해합의 수를 보고 생성자를 찾는 것

n = int(input())
final = 0
for i in range(1, n+1):
    # 분해합의 수가 더 크므로, 생성자가 있다면 이 안에 있을 것
    result = list(map(int, str(i)))
    if n == sum(result)+i:
        # 각 자리의 수와 i의 합이 동일하면 생성자
        final = i
        break
print(final)
