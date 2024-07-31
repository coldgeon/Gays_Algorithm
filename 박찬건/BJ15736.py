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

#이렇게도 가능하다

for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        print(i, n//i)

