N = int(input())

A = list(map(int,input().split()))

A_set = set(A)

M = int(input())

B = list(map(int,input().split()))

for i in range(M):
    if B[i] in A_set:
        print(1)
    else:
        print(0)