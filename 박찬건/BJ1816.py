from sys import stdin


stdin = open("input.txt", "rt")
n = int(stdin.readline().rstrip())

for _ in range(n):
    a = int(stdin.readline().rstrip())
    for i in range(2, 1_000_001): 
        if a % i == 0:
            print("no")
            break
        if i == 1_000_000:
            print("yes")
        
#brute force로 해결하기
#소수를 구하는 법 = 2~해당 숫자까지 전부 나눠보면 됨 허나 아래는 문제 조건으로 백만보다 큰 소수이면 적절한 수라고 함 따라서 아래와 같이 조건을 주는 것임
