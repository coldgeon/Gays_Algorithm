from sys import stdin

stdin = open("input.txt", "rt")
n = int(stdin.readline().rstrip())

for _ in range(n):
    a = 0
    j = int(stdin.readline().rstrip())
    a = sum([k*(sum(z for z in range(1, j+1))+1) for k in range(1, j+1)])
    print(a)