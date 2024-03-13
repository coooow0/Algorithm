T = int(input())
# Quater 25, Dime 10, Nickel 5, Penny 1
for i in range(T):
    cent = int(input())
    Quater = cent / 25
    Dime = cent % 25 / 10
    Nickel = cent % 25 % 10 / 5
    Penny = cent % 25 % 10 % 5 / 1
    print(int(Quater), int(Dime), int(Nickel), int(Penny))
