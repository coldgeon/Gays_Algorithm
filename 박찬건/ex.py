from sys import stdin

stdin = open("input.txt", "rt")
n = int(stdin.readline().rstrip())
cars = map(int, stdin.readline().rsplit(" "))
cnt = 0

for car in cars:
    if n == car:
        cnt += 1

print(cnt)

