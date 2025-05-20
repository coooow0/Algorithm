import sys
input = sys.stdin.readline

color = {
    "black" : 0,
    "brown" : 1,
    "red" : 2,
    "orange" : 3,
    "yellow" : 4,
    "green" : 5,
    "blue" : 6,
    "violet" : 7,
    "grey" : 8,
    "white" : 9
}

a, b, c = [input().strip() for _ in range(3)]
print((color[a] * 10 + color[b]) * (10 ** color[c]))
