#왼쪽에서부터 누적합하고 가장 높은 곳 만나기
#오른쪽에서 누적합하고 가장 높은 곳에서 만나기
#둘이 더하기

from sys import stdin

stdin = open("input.txt", "rt")

n = stdin.readline().rstrip()
arr = [list(map(int, (stdin.readline().rstrip().split()))) for _ in range(int(n))]
print(sorted(arr))
prefix = [ 0 for _ in range(int(n)+1)]


