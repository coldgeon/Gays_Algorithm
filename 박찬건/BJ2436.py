from sys import stdin
from math import gcd, lcm  #최대공약수 module

stdin = open("input.txt", "rt")
a, b = map(int, stdin.readline().split())

maxg = a*b

answer = []

for i in range(a, int(maxg**0.5)+1, a):
    if gcd(i, (maxg//i)) == a:
        if lcm(i, (maxg//i)) == b:
            answer.append((i, maxg//i))
            
print(*answer[-1])
