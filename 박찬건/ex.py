from sys import stdin

stdin = open("input.txt", "rt")
a, b = map(int, stdin.readline().split())
arr = [ int(stdin.readline().rstrip()) for _ in range(a)]

for i in arr:
    print(b//sum(arr) * i)
