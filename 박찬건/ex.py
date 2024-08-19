
#10698 왜 틀림..?
"""
from sys import stdin

stdin = open("input.txt", "rt")
n = int(stdin.readline().rstrip())

for i in range(1, n+1):
    a = stdin.readline().split()
    print(a)
    if a[1] == "+":
        b = int(a[0]) + int(a[2])
        if b == int(a[4]):
            print(b)
            print(f"Case {i}: Yes")
        else:
            print(f"Case {i}: No")
    elif a[1] == "-":
        b = int(a[0]) - int(a[2])
        if b == int(a[4]):
            print(f"Case {i}: Yes")
        else:
            print(f"Case {i}: No")
"""

from sys import stdin
from itertools import combinations

stdin = open("input.txt", "rt")
n, m = map(int, stdin.readline().split())

for i in combinations(range(1, n+1), m):
    print(*i)