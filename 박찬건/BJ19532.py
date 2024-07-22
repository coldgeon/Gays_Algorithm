from sys import stdin

stdin = open("input.txt", "rt")
a, b, c, d, e, f = list(map(int, (stdin.readline().split())))

#1차 시도...50%...
Y = 0
X = 0

for y in range(-999, 1000):
    if a == 0 and b*y-c == 0:
        Y=y
        break
    if d*((-b*y+c)/a) + e*y - f == 0:
        Y = y

for x in range(-999, 1000):
    if a*x + b*Y - c == 0:
        X=x
print(X, Y)


#2차 강의 참고
# 그냥 단순하게 생각하면 됨 어차피 계산은 컴터가 해줌
# 만족하는 식만 뽑으면 된다는 말이다.
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x+b*y == c and d*x+e*y == f:
            print(x, y)
