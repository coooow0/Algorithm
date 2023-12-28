n = int(input())
bag = 0

while n >= 0:
    if n % 5 == 0:  # 5로 나누어 떨어지는 경우
        bag += n // 5  # 5kg 봉지 수를 더해줌
        print(bag)
        break
    n -= 3  # 5로 나누어 떨어지지 않는 경우, 3kg 봉지를 빼주고
    bag += 1  # 3kg 봉지 수를 더해줌
else:  # n이 0보다 작아진 경우, 즉 5kg와 3kg 봉지로 딱 떨어지게 만들 수 없는 경우
    print(-1)
