from sys import stdin

stdin = open("input.txt", "rt")
cnt = 0

while True:
    a = stdin.readline().rstrip()
    b = stdin.readline().rstrip()
    valid = True

    if a == "END":
        break
    a, b = sorted(a), sorted(b)
    cnt += 1

    for i, a_s in enumerate(a):
        if b[i] != a_s or len(a) != len(b):
            valid = False
            break
        else:
            valid = True
    if valid:
        print(f"Case {cnt}: same")
    else:
        print(f"Case {cnt}: different")
