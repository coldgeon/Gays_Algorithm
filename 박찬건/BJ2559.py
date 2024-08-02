from sys import stdin

# 다시 보자...

stdin = open("input.txt", "rt")
n, k = map(int, stdin.readline().split(" "))
arr = list(map(int, stdin.readline().split(" ")))
prefix = [ 0 for _ in range(n+1)]

for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]


answer = []
for i in range(k, n+1):
    answer.append(prefix[i] - prefix[i-k])

print(max(answer))