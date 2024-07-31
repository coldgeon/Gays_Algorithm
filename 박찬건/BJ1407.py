from sys import stdin

stdin = open("input.txt", "rt")
a, b = list(map(int, stdin.readline().split()))
total = 0

for i in range(a, b+1):
    if i%2 != 0:
        total += 1
    else:
        j = 1
        while 2**j <= i:
            if i % (2**(j)) != 0:
                total += 2**(j-1)
                break
            elif i / (2**j) == 1:
                total += 2**j
                break
            else:
                j += 1

print(total)