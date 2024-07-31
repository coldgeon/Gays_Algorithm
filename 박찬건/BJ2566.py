#최댓값 찾기

from sys import stdin

stdin = open("input.txt", "rt")
arr = [ list(map(int, (stdin.readline().split()))) for _ in range(9) ]

maximum = 0
row = 0
col = 0
for i, li in enumerate(arr):
    if max(arr[i]) > maximum:
        maximum = max(arr[i])
        row = arr[i].index(maximum)
        col = i
print(maximum)
print(col+1, row+1)

# print(arr[2].index(78))
