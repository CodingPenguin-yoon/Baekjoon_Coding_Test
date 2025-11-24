N = int(input())
Count = 0
for _ in range(N):
    A = [a for a in input()]
    for i in range(len(A)):
        if A[i] == '(':
            Count += 1
        else:
            Count -= 1
        if Count < 0:
            print("NO")
            break
    else:
        if not Count:
            print("YES")
        else:
            print("NO")

    Count = 0

