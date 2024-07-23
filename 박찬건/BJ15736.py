from sys import stdin

stdin = open("input.txt", "rt")
n = int(stdin.readline().rstrip())
cnt = 0

for i in range(1, n+1):
    if i**2 <= n:
        cnt += 1
    elif i**2 > n:
        break
print(cnt)
