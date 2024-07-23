from sys import stdin

stdin = open("input.txt", "rt")

arr = [sorted([ int(stdin.readline().rstrip()) for _ in range(4) ], reverse=True), sorted([int(stdin.readline().rstrip()) for _ in range(2)], reverse=True)]
print(sum(arr[0][:3])+arr[1][0])
