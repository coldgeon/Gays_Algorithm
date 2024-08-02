from sys import stdin
stdin = open("input.txt", "rt")
n = int(stdin.readline().rstrip())

arr = list(map(int, stdin.readline().split()))
prefix = [ -1000 for _ in range(0, n+1)]

for i in range(n):
    prefix[i+1] = max(prefix[i] + arr[i], arr[i])

    
print(max(prefix))