import sys
input = sys.stdin.readline
n = int(input())
# 양수 a가 n의 약수가 되려면, n이 a의 배수이고, a는 1이아니어야 한다.
# 어떤 수 n의 진짜 약수가 모두 주어질 때, n을 구하라
# 첫째 줄은 n 약수의 개수, 둘째 줄에는 n의 약수(즉 a)
# 약수 = 나머지없이 나눌 수 있는 수
arr = list(map(int, input().split()))
arr.sort()
print(arr[0]*arr[-1])