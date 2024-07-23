"""
https://yesdohyun.tistory.com/60 => 이분 블로그 참고했음

"""

from sys import stdin
from itertools import permutations

stdin = open("input.txt", "rt")
n = int(stdin.readline().rstrip())
baseball = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  #모든 경우의 수 따지기

for _ in range(n):
    num, len_s, len_b = stdin.readline().split()
    len_s, len_b = int(len_s), int(len_b)
    delete = []

    for i in range(len(baseball)):
        s, b = 0, 0
        for j in range(3):  #각 자리 돌리는 거
            if int(num[j]) in baseball[i]:  
                if int(num[j]) == baseball[i][j]:
                    s += 1
                else:
                    b += 1
        if s != len_s or b!=len_b:
            delete.append(baseball[i])
    
    for rm in delete:
        baseball.remove(rm)

print(len(baseball))

