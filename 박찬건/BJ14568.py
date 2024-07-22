#a, b, c에게 줄 수 있는 사탕의 경우의 수는 각각 candy개씩
#brute force로 표현하면?
from sys import stdin

stdin = open("input.txt", "rt")
candy = int(stdin.readline().rstrip())
cnt = 0

for a in range(1, candy+1):
    for b in range(1, candy+1):
        for c in range(1, candy+1):
            if a>=b+2 and c%2==0 and a+b+c==candy:
                cnt += 1

print(cnt)
