N = int(input())

l = [list(input().split()) for _ in range(N)]

C_l = [[]for _ in range(201)]

for i in range(N):
    I = int(l[i][0])
    C_l[I].append(l[i])

[print(*p) for bucket in C_l for p in bucket]